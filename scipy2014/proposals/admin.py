from django.contrib import admin

#from symposion.proposals.actions import export_as_csv_action
from scipy2014.proposals.models import TalkPosterProposal, TutorialProposal, BofProposal, SprintProposal

class TalkPosterProposalAdmin(admin.ModelAdmin):
    model = TalkPosterProposal
    list_display = ['title', 'speaker', 'topic_track', 'domain_symposium']
    list_filter = ['submission_type', 'topic_track', 'domain_symposium']
    """
    actions = [export_as_csv_action("CSV Export", fields=[
        "id",
        "title",
        "speaker",
        "speaker_email",
        "kind",
    ])]
    """

admin.site.register(TalkPosterProposal, TalkPosterProposalAdmin)
admin.site.register(TutorialProposal,
        list_display = ['title', 'speaker', 'track'],
        list_filter = ['track'],
        date_heirarchy='submitted',
        )
admin.site.register(BofProposal, 
        list_display = ['title', 'speaker',],
        date_heirarchy='submitted',
        )
admin.site.register(SprintProposal,
        list_display = ['title', 'speaker',],
        date_heirarchy='submitted',
        )
