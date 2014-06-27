"""Deployment scripts for the scipy 2014 conference website

The command to deploy is:
    fab $TARGET $COMMAND

Where $TARGET is staging || prod || dev (eventually), and $COMMAND
is the task to be run.  $TARGET is a special fabric task that correctly
sets up the environment

Example usage:
$ fab staging deploy
$ fab prod deploy:576a8e4241962464f4ac9c11cd5054e306f2f0d1
$ fab dev deploy:origin/v1.0003
"""

from os.path import join as pjoin
import datetime

from fabric.api import run, env, sudo, put, cd, local, task, require, settings
from fabric.contrib.files import sed, upload_template
from fabtools import supervisor, user
from fabtools.require import deb, nginx, python, mysql
import jinja2


env.disable_known_hosts = True

VENV_DIR = '/home/scipy/venvs/'
REPO = '/home/scipy/site/SciPy-2014'
SITE_PATH = '/home/scipy/site'
GIT_REPO = 'https://github.com/scipy-conference/SciPy-2014.git'


@task
def staging():
    env.update({
        'site': 'citationsneeded.org',
        'rewrite_name': 'citationsneeded.org',
        'upstream': 'citationsneeded_org',
        'available': 'citationsneeded',
        'ssl_cert': '/etc/ssl/certs/citationsneeded.crt',
        'ssl_key': '/etc/ssl/private/citationsneeded.key',
        'hosts': ['citationsneeded.org'],
        'local_settings': 'deployment/staging_settings.py',
    })


@task
def prod():
    env.update({
        'site': 'conference.scipy.org',
        'rewrite_name': 'conference.scipy.org',
        'upstream': 'conference_scipy_org',
        'available': 'conference',
        'ssl_cert': '/etc/ssl/localcerts/star_scipy_org.chained.crt',
        'ssl_key': '/etc/ssl/private/star_scipy_org.key',
        'hosts': ['162.242.221.143'],
        'local_settings': 'deployment/prod_settings.py',
    })


@task
def vagrant():
    """
    Run commands using vagrant
    """
    env.update({
        'site': 'localhost',
        'upstream': 'localhost',
        'rewrite_name': 'citationsneeded.org',
        'available': 'conference',
        'ssl_cert': '/etc/ssl/localcerts/conference.scipy.org.crt',
        'ssl_key': '/etc/ssl/private/conference.scipy.org.key',
        'local_settings': 'deployment/prod_settings.py',
    })
    vc = get_vagrant_config()
    # change from the default user to 'vagrant'
    env.user = vc['User']
    # connect to the port-forwarded ssh
    env.hosts = ['%s:%s' % (vc['HostName'], vc['Port'])]
    # use vagrant ssh key
    env.key_filename = vc['IdentityFile'].strip('"')
    # Forward the agent if specified:
    env.forward_agent = vc.get('ForwardAgent', 'no') == 'yes'


def get_vagrant_config():
    """
    Parses vagrant configuration and returns it as dict of ssh parameters
    and their values
    """
    result = local('vagrant ssh-config', capture=True)
    conf = {}
    for line in iter(result.splitlines()):
        parts = line.split()
        conf[parts[0]] = ' '.join(parts[1:])
    return conf


@task
def dev():
    env.update({
        'site': 'localhost',
        'rewrite_name': 'localhost',
        'upstream': 'localhost',
        'available': 'conference',
        'ssl_cert': '/etc/ssl/localcerts/conference.scipy.org.crt',
        'ssl_key': '/etc/ssl/private/conference.scipy.org.key',
        'local_settings': 'deployment/prod_settings.py',
    })
    env.user = 'vagrant'
    env.hosts = ['127.0.0.1:2222']
    env.key_filename = local(
        'vagrant ssh-CONFIG | grep IdentityFile | cut -f4 -d " "',
        capture=True,
    )


def scipy_do(*args, **kw):
    kw['user'] = 'scipy'
    return sudo(*args, **kw)


@task
def deploy(commit=None):
    require('site', 'upstream', 'available', 'ssl_cert', 'ssl_key', 'hosts',
            'local_settings',
            provided_by=('prod', 'staging', 'dev'))
    install_dependencies()

    update_repo(commit=commit)

    venv_path = deploy_venv()
    deploy_mail(venv_path)
    build_static(venv_path)

    deploy_supervisor()
    restart_gunicorn()

    deploy_nginx()
    restart_nginx()


@task
def update_repo(commit=None):
    require('local_settings', provided_by=('prod', 'staging', 'dev'))
    if commit is None:
        commit = 'origin/master'

    with cd(REPO):
        scipy_do('git fetch')
        scipy_do('git checkout %s' % commit)

    scipy_put('deployment/regenerate.sh', pjoin(SITE_PATH, 'bin/regenerate.sh'))
    scipy_put(env['local_settings'],
              pjoin(REPO, 'scipy2014/local_settings.py'))
    scipy_do('cp ~/secrets.py %s' % pjoin(REPO, 'scipy2014', 'secrets.py'))


def build_static(venv_path):
    activate_cmd = 'source %s' % pjoin(VENV_DIR, venv_path, 'bin/activate')
    collect_cmd = 'python manage.py collectstatic --noinput --clear'
    with cd(REPO):
        scipy_do(activate_cmd + ' && ' + collect_cmd)
    scipy_do('chmod -R a+rx %s' % pjoin(SITE_PATH, 'site_media'))


@task
def deploy_nginx():
    require('site', 'upstream', 'available', 'ssl_cert', 'ssl_key',
            provided_by=('prod', 'staging', 'dev'))
    render_to_file('deployment/nginx_conf_template', 'nginx_conf',
                   server_name=env['site'],
                   rewrite_name=env['rewrite_name'],
                   ssl_cert=env['ssl_cert'],
                   ssl_key=env['ssl_key'],
                   upstream=env['upstream'])
    put('nginx_conf',
        pjoin('/etc/nginx/sites-available/', env['available']),
        use_sudo=True)
    nginx.enabled(env['available'])
    nginx.disabled('default')
    #install_certs()


@task
def deploy_supervisor():
    upload_template('deployment/scipy2014.conf',
                    '/etc/supervisor/conf.d/scipy2014.conf',
                    use_sudo=True)
    supervisor.update_config()


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
    render_to_file('deployment/runserver_template.sh',
                   'runserver.sh',
                   virtualenv=venv)
    scipy_put('runserver.sh', pjoin(SITE_PATH, 'bin/runserver.sh'),
              mode='0755')


@task
def restart_gunicorn():
    sudo('supervisorctl restart scipy2014')


@task
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


#def install_certs():
#    put('citationsneeded.crt', '/etc/ssl/certs/citationsneeded.crt',
#        use_sudo=True, mode=0400)
#    put('citationsneeded.key', '/etc/ssl/private/citationsneeded.key',
#        use_sudo=True, mode=0400)


@task
def deploy_mail(venv_path):
    render_to_file('deployment/django_mail_template.sh', 'django_mail.sh',
                   virtualenv=venv_path)
    scipy_put('django_mail.sh', pjoin(SITE_PATH, 'bin/django_mail.sh'),
              mode=0500)


@task
def provision():
    install_dependencies()
    install_python_packages()
    configure_ssh()
    setup_user()
    setup_sitepaths()
    #setup_db()
    print("YOU HAVE TO SETUP MYSQL MANUALLY")


"""
# this does not at all work but something similar could
def setup_db():
    with settings(mysql_user='root', password='notapassword'):
        mysql.user('scipy', password='notapassword')
        mysql.database('scipy2014', owner='scipy')
"""


def setup_user():
    if not user.exists('scipy'):
        sudo('useradd -s/bin/bash -d/home/scipy -m scipy')


def configure_ssh():
    sed('/etc/ssh/sshd_config',
        '^#PasswordAuthentication yes',
        'PasswordAuthentication no',
        use_sudo=True)
    sudo('service ssh restart')


def setup_sitepaths():
    scipy_do('mkdir -p ~/site ~/venvs')
    scipy_do('mkdir -p ~/site/site_media')
    scipy_do('mkdir -p ~/site/site_media/static')
    scipy_do('mkdir -p ~/site/site_media/media')
    with cd(SITE_PATH):
        scipy_do('mkdir -p bin logs')
        scipy_do('git clone %s' % GIT_REPO)
    scipy_do('mkdir -p ~/site/site_media')


def install_dependencies():
    deb.uptodate_index(max_age={'hour': 1})
    deb.packages([
        'python-software-properties',
        'python-dev',
        'build-essential',
        'nginx',
        'libxslt1-dev',
        'supervisor',
        'git',
        'tig',
        'vim',
        'multitail',
        'curl',
        'tmux',
        'htop',
        'ack-grep',
        'libmysqlclient-dev',
        'mysql-server',
        'mysql-client',
        'python-mysqldb',
        'libjpeg-dev',
        'libtiff-dev',
        'zlib1g-dev',
        'python-virtualenv',
    ])


@task
def install_php_dependencies():
    deb.packages([
        "php5",
        "php5-fpm",
        "php-pear",
        "php5-common",
        "php5-mcrypt",
        "php5-mysql",
        "php5-cli",
        "php5-gd",
    ])


def install_python_packages():
    sudo('wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py')
    sudo('python get-pip.py')
    # install global python packages
    python.packages(['virtualenvwrapper', 'setproctitle'], use_sudo=True)
