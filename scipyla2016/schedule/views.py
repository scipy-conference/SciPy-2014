from django.shortcuts import render

from models import PosterPresentation
from scipyla2016.proposals.models import SprintProposal


def poster_list(request):
    posters = PosterPresentation.objects.filter(cancelled=False)
    ctx = {
        'posters': posters,
    }
    return render(request, "schedule/poster_list.html", ctx)


def sprint_list(request):
    sprints = SprintProposal.objects.filter(presentation__isnull=False)
    ctx = {
        'presentations': [sprint.presentation for sprint in sprints],
    }
    return render(request, "schedule/sprint_list.html", ctx)
