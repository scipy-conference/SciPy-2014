from os.path import join as pjoin
import datetime

from fabric.api import run, env, sudo, put, cd
import jinja2


env.hosts = ['mrterry@citationsneeded.org']
VENV_DIR = '/home/scipy/venvs/'
SITE = 'citationsneeded.org'
REPO = '/home/scipy/site/SciPy-2014'
SITE_PATH = '/home/scipy/site'

UPSTREAM = SITE.replace('.', '_')
AVAILALBE = SITE.split('.')[0]


def scipy_do(*args, **kw):
    kw['user'] = 'scipy'
    return sudo(*args, **kw)


def deploy(commit=None):
    update_repo(commit=commit)

    venv_path = deploy_venv()
    deploy_mail(venv_path)
    build_static(venv_path)
    restart_gunicorn()

    deploy_nginx()
    restart_nginx()


def update_repo(commit=None):
    if commit is None:
        commit = 'origin/master'

    with cd(REPO):
        scipy_do('git fetch')
        scipy_do('git checkout %s' % commit)

    scipy_put('rackspace_settings.py',
              pjoin(REPO, 'scipy2014/local_settings.py'))
    scipy_do('cp ~/secrets.py %s' % pjoin(REPO, 'scipy2014', 'secrets.py'))


def build_static(venv_path):
    activate_cmd = 'source %s' % pjoin(VENV_DIR, venv_path, 'bin/activate')
    collect_cmd = 'python manage.py collectstatic --noinput --clear'
    with cd(REPO):
        scipy_do(activate_cmd + ' && ' + collect_cmd)
    scipy_do('chmod -R a+rx %s' % pjoin(SITE_PATH, 'site_media'))


def deploy_nginx():
    render_to_file('nginx_conf_template', 'nginx_conf',
                   server_name=SITE, upstream=UPSTREAM)
    put('nginx_conf', pjoin('/etc/nginx/sites-available/', AVAILALBE),
        use_sudo=True)
    #install_certs()


def build_venv():
    with cd(REPO):
        commit = run('git rev-parse HEAD').strip()
    venv_path = pjoin(VENV_DIR, commit)
    activate = 'source %s' % pjoin(venv_path, 'bin/activate')
    install = 'pip install -r %s' % pjoin(REPO, 'requirements.txt')

    dirs = run('ls %s' % VENV_DIR).split()
    if commit not in dirs:
        print "Virtual env for commit doesn't exist.  Creating."
        scipy_do('virtualenv %s' % venv_path)
        scipy_do(activate + ' && ' + install)
    else:
        print 'Virtual env exists.'

    today = datetime.date.today().isoformat()
    new_venvs = [d for d in dirs if d.startswith(today)]
    new_venvs.sort()
    human_path = today + '.%i' % len(new_venvs)
    with cd(VENV_DIR):
        scipy_do('ln -s %s %s' % (commit, human_path))
    return pjoin(VENV_DIR, human_path)


def deploy_venv():
    venv_path = build_venv()
    put_gunicorn_conf(venv_path)
    return venv_path


def put_gunicorn_conf(venv):
    render_to_file('runserver_template.sh', 'runserver.sh', virtualenv=venv)
    scipy_put('runserver.sh', pjoin(SITE_PATH, 'bin/runserver.sh'),
              mode='0755')


def restart_gunicorn():
    sudo('supervisorctl restart scipy2014')


def restart_nginx():
    sudo('service nginx restart')


def scipy_put(local_path, dest_path, **kw):
    kw['use_sudo'] = True
    put(local_path, dest_path, **kw)
    sudo('chown scipy %s' % dest_path)


def render_to_file(template_path, output_path, **kw):
    with open(template_path) as f:
        template = jinja2.Template(f.read())
    conf = template.render(**kw)
    with open(output_path, 'w') as f:
        f.write(conf)


def install_certs():
    put('citationsneeded.crt', '/etc/ssl/certs/citationsneeded.crt',
        use_sudo=True, mode=0400)
    put('citationsneeded.key', '/etc/ssl/private/citationsneeded.key',
        use_sudo=True, mode=0400)


def deploy_mail(venv_path):
    render_to_file('django_mail_template.sh', 'django_mail.sh',
                   virtualenv=venv_path)
    scipy_put('django_mail.sh', pjoin(SITE_PATH, 'bin/django_mail.sh'))
