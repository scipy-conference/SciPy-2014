from django.db import models

from markitup.fields import MarkupField

from scipy2014.proposals.models import TalkPosterProposal

"""

Last minute hack to throw together a poster schedule list page based on csv file

CSV file has these headings
#id,speaker,title,category,domain

the database is populated via the schedule management command, create_poster_list

"""

class PosterPresentation(models.Model):
    TOPICS = (
        ('General', 'General'),
        ('Scientific_Computing_Education', 'Scientific Computing Education'),
        ('Geospatial_Data_in_Science', 'Geospatial Data in Science'),
    )
    DOMAINS = (
        ('None', 'None'),
        ('Astronomy_and_Astrophysics', 'Astronomy and Astrophysics'),
        ('Bioinformatics', 'Bioinformatics'),
        ('Engineering', 'Engineering'),
        ('Geophysics', 'Geophysics'),
        ('Computation_Social_Sciences_and_Digital_Humanities', 'Computation Social Sciences and Digital Humanities'),
        ('Vision_Visualization_and_Imaging', 'Vision, Visualization, and Imaging'),
    )
    domain = models.CharField(max_length=100, choices=DOMAINS, default='None')
    topic = models.CharField(max_length=100, choices=TOPICS, default='General')
    title = models.CharField(max_length=100)
    description = MarkupField()
    abstract = MarkupField()
    speaker = models.CharField(max_length=100)
    cancelled = models.BooleanField(default=False)
    proposal = models.OneToOneField(TalkPosterProposal, related_name="posterpresentation")

    @property
    def number(self):
        return self.proposal.number
    
    def __unicode__(self):
        return "#%s %s (%s)" % (self.number, self.title, self.speaker)
 
