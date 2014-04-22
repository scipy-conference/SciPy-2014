from django.db import models

from symposion.proposals.models import ProposalBase


class TalkPosterProposal(ProposalBase):

    TYPE_TALK_OR_POSTER = 1
    TYPE_TALK_ONLY = 2
    TYPE_POSTER_ONLY = 3

    SUBMISSION_TYPES = [
        (TYPE_TALK_OR_POSTER, "Talk or Poster"),
        (TYPE_TALK_ONLY, "Talk Only"),
        (TYPE_POSTER_ONLY, "Poster Only"),
    ]
    submission_type_lookup = dict(SUBMISSION_TYPES)

    TRACK_GENERAL = 1
    TRACK_MACHINE_LEARNING = 2
    TRACK_TOOLS = 3
    TRACK_DOMAIN_ONLY = 4
    TRACK_EDUCATION = 5
    TRACK_GIS = 6

    TOPIC_TRACKS = [
        (TRACK_GENERAL, "General"),
        (TRACK_EDUCATION, 'Scientific Computing Education'),
        (TRACK_GIS, 'Geospatial Data in Science'),
    ]
    track_lookup = dict(TOPIC_TRACKS)

    DOMAIN_NONE = 1
    DOMAIN_MEDICAL_IMAGING = 2
    DOMAIN_METEOROLOGY = 3
    DOMAIN_ASTRONOMY = 4
    DOMAIN_BIO_INFORMATICS = 5
    DOMAIN_GEOPHYSICS = 6
    DOMAIN_VISUALIZATION = 7
    DOMAIN_SOCIAL = 8
    DOMAIN_ENGINEERING = 9
    DOMAIN_SOCIAL_SCIENCES_AND_HUMANITIES = 10

    DOMAIN_SYMPOSIA = [
        (DOMAIN_NONE, "None, only submit to tracks"),
        (DOMAIN_ASTRONOMY, 'Astronomy and Astrophysics'),
        (DOMAIN_BIO_INFORMATICS, 'Bioinformatics'),
        (DOMAIN_GEOPHYSICS, 'Geophysics'),
        (DOMAIN_VISUALIZATION, 'Vision, Visualization, and Imaging'),
        (DOMAIN_ENGINEERING, 'Engineering'),
        (DOMAIN_SOCIAL_SCIENCES_AND_HUMANITIES, 'Computational Social Sciences and Digital Humanities'),
    ]
    domain_lookup = dict(DOMAIN_SYMPOSIA)

    submission_type = models.IntegerField(choices=SUBMISSION_TYPES, default=1)
    topic_track = models.IntegerField(choices=TOPIC_TRACKS, default=1)
    domain_symposium = models.IntegerField(choices=DOMAIN_SYMPOSIA, default=1)

    def topic_track_display(self):
        return self.track_lookup.get(self.topic_track, '')
    def domain_symposium_display(self):
        return self.domain_lookup.get(self.domain_symposium, '')
    def submission_type_display(self):
        return self.submission_type_lookup.get(self.domain_symposium, '')


    class Meta:
        verbose_name = "talk/poster proposal"


class TutorialProposal(ProposalBase):

    TRACK_INTRODUCTORY = 1
    TRACK_INTERMEDIATE = 2
    TRACK_ADVANCED = 3

    TRACKS = [
        (TRACK_INTRODUCTORY, "Introductory"),
        (TRACK_INTERMEDIATE, "Intermediate"),
        (TRACK_ADVANCED, "Advanced"),
    ]
    track_lookup = dict(TRACKS)

    track = models.IntegerField(choices=TRACKS)

    package_list = models.TextField(
        "Package List",
        help_text="""A list of Python packages that attendees will need to
have installed prior to the class to follow along. Please mention if
any packages are not cross platform. Installation instructions or
links to installation documentation should be provided for packages
that are not available through easy_install, pip, Canopy, Anaconda
etc., or that require third party libraries."""
    )

    def track_display(self):
        return self.track_lookup.get(self.track, '')

    class Meta:
        verbose_name = "tutorial proposal"


class BofProposal(ProposalBase):
    class Meta:
        verbose_name = "birds of a feather proposal"


class SprintProposal(ProposalBase):
    class Meta:
        verbose_name = "sprint proposal"
