from django.shortcuts import render

from symposion.reviews.models import ProposalResult

"""
HACK

This year we used TalkPosterProposals, which buckets posters and talks. Next
year we should not do this. We should have separate proposals for each.

We want to have a page where people can view the list of accepted posters.
For a workaround, the convention will be to leave the review status as
'standby' for all posters.
"""


def standby_list(request):
    results = ProposalResult.objects.filter(status='standby')
    ctx = {
        "proposals": [r.proposal for r in results],
    }
    return render(request, "posters.html", ctx)
