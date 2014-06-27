#!/bin/bash


${VIRTUAL_ENV:?"Activate virtualenv before calling this"}

DJANGODIR=/home/scipy/site/SciPy-2014/

set -evx

cd $DJANGODIR

./manage.py delete_schedule
./manage.py create_schedule data/slotkinds.csv -m slotkinds
./manage.py create_schedule data/rooms.csv -m rooms
./manage.py create_schedule data/tutorials.csv 
./manage.py create_schedule data/talksposters.csv 
./manage.py create_schedule data/bofs.csv 
./manage.py create_schedule data/sprints.csv 
