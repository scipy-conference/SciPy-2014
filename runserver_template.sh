#!/bin/bash

set -e
NAME="scipy"
VIRTUALENV={{ virtualenv }}
SITE_ROOT=/home/scipy/site
#LOGDIR=${SITE_ROOT}/logs/
#LOGFILE=${LOGDIR}/output.log
DJANGODIR=${SITE_ROOT}/SciPy-2014/
#SOCKFILE=${SITE_ROOT}/run/gunicorn.sock
PORT=8000
BIND_IP=127.0.0.1:$PORT
USER=scipy
GROUP=scipy
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=scipy2014.settings
DJANGO_WSGI_MODULE=scipy2014.wsgi

echo "Starting $NAME as `whoami`"
echo "Activating $VIRTUALENV"
source ${VIRTUALENV}/bin/activate


cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --bind $BIND_IP
