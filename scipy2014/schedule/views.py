from django.shortcuts import render

from models import PosterPresentation

def poster_list(request):
    posters = PosterPresentation.objects.filter(cancelled=False)
    ctx = {
        'posters': posters,
    }
    return render(request, "schedule/poster_list.html", ctx)
