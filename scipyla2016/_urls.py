from django.conf import settings
from django.conf.urls.defaults import patterns, url, include
from django.conf.urls.static import static

from django.views.generic.simple import direct_to_template

from django.contrib import admin

import symposion.views

from scipyla2016.schedule.views import poster_list, sprint_list

from sitetree.sitetreeapp import register_i18n_trees


register_i18n_trees(['main'])

urlpatterns = patterns(
    "",
    url(r"^$",
        direct_to_template,
        {"template": "homepage.html"},
        name="home"),
    url(r"^about/$",
        direct_to_template,
        {"template": "about/about.html"},
        name="about"),
    url(r'^venue/$',
        direct_to_template,
        {'template': 'venue/venue.html'},
        name='venue'),
    url(r'^lodging/$',
        direct_to_template,
        {'template': 'venue/lodging.html'},
        name='lodging'),
    url(r'^directions/$',
        direct_to_template,
        {'template': 'venue/directions.html'},
        name='directions'),
    url(r'^floorplans/$',
        direct_to_template,
        {'template': 'venue/floorplans.html'},
        name='floorplans'),
    url(r'^restaurants/$',
        direct_to_template,
        {'template': 'venue/restaurants.html'},
        name='restaurants'),
    url(r'^plotting_contest/$',
        direct_to_template,
        {'template': 'participate/plotting_contest.html'},
        name='plotting_contest'),
    url(r'^organizers/$',
        direct_to_template,
        {'template': 'about/organizers.html'},
        name='organizers'),
    url(r'^diversity/$',
        direct_to_template,
        {'template': 'about/diversity.html'},
        name='diversity'),
    url(r'^code_of_conduct/$',
        direct_to_template,
        {'template': 'about/code_of_conduct.html'},
        name='code_of_conduct'),
    url(r"^admin/", include(admin.site.urls)),
    url(r'^video_highlights/$',
        direct_to_template,
        {'template': 'video_highlights.html'},
        name='video highlights'),
    url(r'^privacy_policy/$',
        direct_to_template,
        {'template': 'privacy_policy.html'},
        name='privacy_policy'),
    url(r'^sponsorship/$',
        direct_to_template,
        {'template': 'sponsorship.html'},
        name='sponsorship'),
    url(r'^sponsor_levels/$',
        direct_to_template,
        {'template': 'sponsor_levels.html'},
        name='sponsor_levels'),
    url(r'^keynotes/$',
        direct_to_template,
        {'template': 'keynotes.html'},
        name='keynotes'),
    url(r'^participate/bofs/$',
        direct_to_template,
        {'template': 'participate/bofs.html'}),
    url(r'^participate/presentations/$',
        direct_to_template,
        {'template': 'participate/presentations.html'}),
    url(r'^participate/tutorials/$',
        direct_to_template,
        {'template': 'participate/tutorials.html'},
        name='tutorials'),
    url(r'^participate/plotting_contest/$',
        direct_to_template,
        {'template': 'participate/plotting_contest.html'},
        name='plotting_contest'),
    url(r'^participate/sprints/$',
        direct_to_template,
        {'template': 'participate/sprints.html'},
        name='sprints'),
    url(r'^participate/financial_aid/$',
        direct_to_template,
        {'template': 'participate/financial_aid.html'}),
    url(r'^participate/wssspe/$',
        direct_to_template,
        {'template': 'participate/wssspe.html'}),
    url(r'^participate/ambassadors/$',
        direct_to_template,
        {'template': 'participate/ambassadors.html'},
        name='ambassadors'),
    url(r"^account/signup/$",
        symposion.views.SignupView.as_view(),
        name="account_signup"),
    url(r"^account/login/$",
        symposion.views.LoginView.as_view(),
        name="account_login"),
    url(r"^account/", include("account.urls")),

    url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),
    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposals/", include("symposion.proposals.urls")),
    url(r"^sponsors/", include("symposion.sponsorship.urls")),
    url(r"^boxes/", include("symposion.boxes.urls")),
    url(r"^teams/", include("symposion.teams.urls")),
    url(r"^reviews/", include("symposion.reviews.urls")),
    url(r"^schedule/", include("symposion.schedule.urls")),
    url(r"^markitup/", include("markitup.urls")),

    url(r"^posters/", poster_list, name="poster_list"),
    url(r"^sprints/", sprint_list, name="sprint_list"),

    url(r"^", include("symposion.cms.urls")),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^site_media/media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
