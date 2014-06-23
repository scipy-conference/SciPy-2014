import csv
import os
import re

from django.core.management.base import BaseCommand
from django.db import transaction


from scipy2014.proposals.models import TalkPosterProposal
from scipy2014.schedule.models import PosterPresentation


def create_poster_presentation(data):

    for row in data:
        #id,speaker,title,category,domain
        try:
            proposal = TalkPosterProposal.objects.get(pk=row['id'])
        except TalkPosterProposal.DoesNotExist:
            print 'No proposal found, skipping row %s' % row
            continue

        topic = re.sub(r' ', '_', row.get('category', 'General'))
        domain = re.sub(r' ', '_', row.get('domain', 'None'))

        poster = PosterPresentation(
            title = row['title'],
            speaker = row['speaker'],
            topic = topic,
            domain = domain, 
            abstract = proposal.abstract,
            description = proposal.description,
            proposal = proposal
        )
        poster.save()


def get_csv_data(csvfile):
    with open(csvfile) as fh:
        reader = csv.DictReader(fh)
        return [dict((k.strip(), v.strip()) for k, v in x.items()) for x in reader]


class Command(BaseCommand):
    args = 'csvfile'
    help = """
    Clobber any current poster presentations and create new ones

    id,speaker,title,category,domain
    107,Aaron Meurer,SymPy: Symbolic math for Python,General,None
    """

    @transaction.commit_on_success
    def handle(self, *args, **options):
        assert os.path.isfile(args[0]), 'not a file: %s' % args[0]

        data = get_csv_data(args[0])

        PosterPresentation.objects.all().delete()

        create_poster_presentation(data)
