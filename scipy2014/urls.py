from django.conf.urls.defaults import patterns, include
from django.contrib import admin
admin.autodiscover()

# from pinax.apps.account.openid_consumer import PinaxConsumer

WIKI_SLUG = r"(([\w-]{2,})(/[\w-]{2,})*)"

urlpatterns = patterns(
    '',
    (r'^scipy2014/', include('scipy2014._urls')),
)
