
from django.shortcuts import redirect
from django.conf.urls.defaults import patterns, include
from django.contrib import admin
admin.autodiscover()

# from pinax.apps.account.openid_consumer import PinaxConsumer

WIKI_SLUG = r"(([\w-]{2,})(/[\w-]{2,})*)"

urlpatterns = patterns(
    '',
    (r'^$', lambda r: redirect("scipyla2016/", permanent=True)),
    (r'^scipyla2016/', include('scipyla2016._urls')),
)
