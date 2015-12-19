# SciPyLA 2016

Website for the SciPyLA Conference 2016.

## Dependencies

-   Python
-   virtualenv

## Quickstart

~~~
$ git clone git@github.com:scipy-latinamerica/website-scipyla2016.git
$ cd website-scipyla2016
$ virtualenv .
$ source bin/activate
$ pip install -r requirements.txt
$ python manage.py syncdb
$ python manage.py loaddata fixtures/*
$ python manage.py runserver
~~~

Open http://localhost:8000/scipyla2016/ on your web browser
to preview the web site.

## Administration

Open http://localhost:8000/scipyla2016/admin/
and log in with the email address and password
that you provide during the quickstart.

If you forgot the email address and password
use

~~~
$ python manage.py createsuperuser
~~~
