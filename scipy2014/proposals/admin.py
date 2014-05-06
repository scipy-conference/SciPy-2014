from django.contrib import admin

#from symposion.proposals.actions import export_as_csv_action
from scipy2014.proposals.models import TalkPosterProposal, TutorialProposal, BofProposal, SprintProposal

class TalkPosterProposalAdmin(admin.ModelAdmin):
    model = TalkPosterProposal
    list_display = [
        'title',
        'speaker',
        'speaker_email',
        'topic_track',
        'domain_symposium',
        'kind',
        'cancelled',
    ]
    list_filter = ['submission_type', 'topic_track', 'domain_symposium', 'cancelled']

admin.site.register(TalkPosterProposal, TalkPosterProposalAdmin)
admin.site.register(TutorialProposal,
        list_display = ['title', 'speaker', 'speaker_email', 'track', 'cancelled'],
        list_filter = ['track'],
        date_heirarchy='submitted',
        )
admin.site.register(BofProposal, 
        list_display = ['title', 'speaker', 'speaker_email', 'cancelled'],
        date_heirarchy='submitted',
        )
admin.site.register(SprintProposal,
        list_display = ['title', 'speaker', 'speaker_email', 'cancelled'],
        date_heirarchy='submitted',
        )
