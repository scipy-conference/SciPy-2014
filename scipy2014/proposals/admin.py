from django.contrib import admin

from scipy2014.proposals.models import TalkPosterProposal, TutorialProposal, BofProposal, SprintProposal


admin.site.register(TalkPosterProposal)
admin.site.register(TutorialProposal)
admin.site.register(BofProposal)
admin.site.register(SprintProposal)
