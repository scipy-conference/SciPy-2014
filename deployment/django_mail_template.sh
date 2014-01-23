#!/bin/bash

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


set -e
VIRTUALENV={{ virtualenv }}
DJANGODIR=/home/scipy/site/SciPy-2014/
DJANGO_SETTINGS_MODULE=scipy2014.settings
DJANGO_WSGI_MODULE=scipy2014.wsgi

echo "Starting django-mailer: $MAILCMD"
echo "Activating $VIRTUALENV"
source ${VIRTUALENV}/bin/activate

cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

./manage.py $MAILCMD

echo "done with django-mailer: $MAILCMD"
