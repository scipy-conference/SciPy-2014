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

## Dump data

Some configuration are stored on `fixtures/`
that are load with

~~~
$ python manage.py loaddata fixtures/*
~~~

and need to be run

~~~
$ python manage.py dumpdata --indent=4 boxes.box > fixtures/boxes_box.json
$ python manage.py sitetreedump --indent=4 > fixtures/sitetree.json
$ python manage.py dumpdata --indent=4 conference.conference conference.section > fixtures/conference.json
$ python manage.py dumpdata --indent=4 sites.site > fixtures/initial_data.json
$ python manage.py dumpdata --indent=4 proposals.proposalkind proposals.proposalsection > fixtures/proposal_base.json
$ python manage.py dumpdata --indent=4 sponsorship.benefit sponsorship.benefitlevel > fixtures/sponsor_benefits.json
$ python manage.py dumpdata --indent=4 sponsorship.sponsorlevel > fixtures/sponsor_levels.json
~~~

## Translation

Please read https://docs.djangoproject.com/en/1.9/topics/i18n/translation/#localization-how-to-create-language-files.

## Issues

Please create issues at https://github.com/scipy-latinamerica/scipyla2016/issues.
