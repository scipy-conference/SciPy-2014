from django.core.management.base import BaseCommand
from django.db import transaction

from symposion.reviews.models import promote_proposal
from scipyla2016.proposals.models import SprintProposal


class Command(BaseCommand):
    help = """
    Create Presentations for accepted Sprints.

    If Presentations already exist, does nothing.
    """

    @transaction.commit_on_success
    def handle(self, *args, **options):
        accepted_sprints = SprintProposal.objects.filter(result__status='accepted')
        for sprint in accepted_sprints:
            promote_proposal(sprint)

