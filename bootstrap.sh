#!/usr/bin/env bash

# This automates things according to suggestions from "Setting up Django with Nginx,
# Gunicorn, virtualenv, supervisor and PostgreSQL" but with a few differences.
# http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/
#
# NOTE: Matt has a fabfile written after this and we should use that. but
# meanwhile, here is something to use interact with vagrant fabtools is one
# package that works with fabfile to interact with vagrant, and we can evaluate
# that or work with something you are more familiar with

set -e

SECRETS_BASE=$PWD
if [ -z "$1" ]; then
    echo "using default environment: local"
else
    case "$1" in
        local) ;;
        prod) ;;
        staging) ;;
        vagrant) SECRETS_BASE=/vagrant ;;
        *) echo "invalid environment: $1"; echo "usage: bootstrap.sh <local|prod|staging|vagrant>"; exit ;;
    esac
    ENVIRONMENT="$1"
fi

ENVIRONMENT_DIR=${SECRETS_BASE}/${ENVIRONMENT}
if [ ! -d "$ENVIRONMENT_DIR" ]; then
    echo "stop! missing environment: $ENVIRONMENT_DIR"
    exit 2
    
fi

apt-get update -y

# some requirements and some nice to haves
apt-get install -y python-software-properties \
    python-dev \
    build-essential \
    python-pip \
    nginx \
    libxslt1-dev \
    supervisor \
    git \
    postgresql \
    postgresql-server-dev-9.1 \
    vim \
    exuberant-ctags \
    multitail \
    curl \
    tmux \
    htop \
    ack-grep \
    tig

pip install virtualenvwrapper
pip install setproctitle # or just in a virtualenv?

# Lock things down a little
sed -i -e 's/^#PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config
echo DebianBanner no >> /etc/ssh/sshd_config
service ssh restart

useradd -s/bin/bash -d/home/scipy2014 -m scipy2014
su postgres -c 'createuser -S -D -R -w scipy2014'
su postgres -c 'createdb -w -O scipy2014 scipy2014'

cat << 'ALIASES' > /home/scipy2014/.bash_aliases
if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
    . /usr/local/bin/virtualenvwrapper.sh
fi
export WORKON_HOME=${HOME}/venvs
ALIASES
chown scipy2014:scipy2014 /home/scipy2014/.bash_aliases

cd ~scipy2014
su scipy2014 -c 'mkdir venvs'
su scipy2014 -c 'mkdir site'
cd site
su scipy2014 -c 'mkdir bin logs'
#su scipy2014 -c 'mkdir env'
su scipy2014 -c 'git clone git://github.com/scipy-conference/SciPy-2014'

cat << 'RUNSERVER' > /home/scipy2014/site/bin/runserver.sh
#!/bin/bash

set -e
NAME=scipy2014conf
HOMEDIR=/home/scipy2014
DJANGODIR=${HOMEDIR}/site/SciPy-2014/
VIRTUALENV=${HOMEDIR}/venvs/scipy2014 # TODO un-hardcode
PORT=8000
BIND_IP=127.0.0.1:$PORT # TODO un-hardcode
USER=`whoami`
GROUP=scipy2014 # TODO un-hardcode
NUM_WORKERS=3
DJANGO_WSGI_MODULE=scipy2014.wsgi
LOG_LEVEL=debug

echo "Starting $NAME as $USER with $VIRTUALENV"
source ${VIRTUALENV}/bin/activate

cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=scipy2014.settings
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER \
  --group=$GROUP \
  --log-level=$LOG_LEVEL \
  --bind $BIND_IP
RUNSERVER

# TODO: need to scrip adding the cronjob
#* * * * * (/home/scipy2014/site/bin/django_mail.sh send_mail >> /home/scipy2014/site/logs/cron_mail.log 2>&1)
#0,20,40 * * * * (/home/scipy2014/site/bin/django_mail.sh retry_deferred.sh >> /home/scipy2014/site/logs/cron_mail.log 2>&1)
cat << 'DJANGO_MAILER' > /home/scipy2014/site/bin/django_mail.sh
#!/bin/bash

set -e

if [ -z "$1" ]; then
    echo "usage: django_mail.sh <send_mail|retry_deferred>"
    exit
fi

MAILCMD=$1
case "$MAILCMD" in
    send_mail) ;;
    retry_deferred) ;;
    *) echo "invalid option: $MAILCMD"; exit ;;
esac

HOMEDIR=/home/scipy2014
DJANGODIR=${HOMEDIR}/site/SciPy-2014/
VIRTUALENV=${HOMEDIR}/venvs/scipy2014 # TODO un-hardcode

echo "Starting django-mailer: $MAILCMD with $VIRTUALENV"
source ${VIRTUALENV}/bin/activate

cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=scipy2014.settings
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

./manage.py $MAILCMD

echo "done with django-mailer: $MAILCMD"
DJANGO_MAILER

# how will we generate a secret key to go in our settings file?
#tr -dc '[:alnum:]~@#%^&*-_' < /dev/urandom | head -c 128 > /home/scipy2014/site/env/SECRET_KEY

chmod +x /home/scipy2014/site/bin/runserver.sh
chmod +x /home/scipy2014/site/bin/django_mail.sh
chown -R scipy2014:scipy2014 /home/scipy2014/site/

cat << 'NGINX' > /etc/nginx/sites-available/scipy2014conf
upstream scipy2014conf {
    server 127.0.0.1:8000;
}

# TODO I don't know how to make ssl work for vagrant!
server {
    listen 80;
    server_name .scipy.org;
    client_max_body_size 10M;

    access_log /home/scipy2014/site/logs/scipy.access.log;
    error_log /home/scipy2014/site/logs/scipy.error.log;

    location /site_media/media/ {
        alias /home/scipy2014/site/site_media/static/media;
    }

    # TODO do we want this and if so, how to configure it?
    #location /nginx_status {
    #    stub_status on;
    #    access_log off;
    #    allow {{ nginx_status_allowed_host }};
    #    deny all;
    #}


    location /site_media/static/ {
        alias /home/scipy2014/site/site_media/;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        #proxy_set_header X-Forwarded-Ssl on;  # experimental
        proxy_set_header Host $host;
        proxy_pass http://scipy2014conf;
    }
}
NGINX
unlink /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/scipy2014conf /etc/nginx/sites-enabled/
service nginx restart

# TODO add autorestart?
cat << 'SUPERVISOR' > /etc/supervisor/conf.d/scipy2014.conf
[program:scipy2014]
command = /home/scipy2014/site/bin/runserver.sh
user = scipy2014
group = scipy2014
autostart = true
stdout_logfile = /home/scipy2014/site/logs/gunicorn_supervisor.log
redirect_stderr = true
SUPERVISOR

# TODO don't restart nginx and update supervisor until we get settings worked out
# ideas: vagrant mounts /vagrant to the current directory, and we can 
# distribute secrets out of band and have them go in $ENVIRONMENT_DIR 
# which is a subdir of something we .gitignore 
#
# when we establish that practice, we can add things to bootstrap django
cd ~scipy2014/site/Scipy-2014/
su scipy2014 -c 'wget http://effbot.org/downloads/Imaging-1.1.7.tar.gz' 
su scipy2014 -c 'mkvirtualenv scipy2014'
su scipy2014 -c 'pip install -r requirements.txt'
# TODO get local settings
#su scipy2014 -c './manage.py syncdb --noinput'
# TODO don't know how to script creating a superuser. you can't load fixtures without user 1
# once you have a user and local settings
# TODO su scipy2014 -c './manage.py collectstatus'
# TODO su scipy2014 -c './manage.py loaddata fixtures/*'

# TODO don't run these until we work out getting the above
#supervisorctl reread
#supervisorctl update
