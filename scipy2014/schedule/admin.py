from django.contrib import admin

from scipy2014.schedule.models import PosterPresentation

class PosterPresentationAdmin(admin.ModelAdmin):
    model = PosterPresentation
    list_display = [
        'title',
        'speaker',
        'domain',
        'topic',
        'cancelled',
    ]
    list_filter = [
        'domain',
        'topic',
        'cancelled',
    ]

admin.site.register(PosterPresentation, PosterPresentationAdmin)
