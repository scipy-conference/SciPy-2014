from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('scipy2014.posters.views',
    url(r'^$', 'standby_list', name='standbys'),
)
