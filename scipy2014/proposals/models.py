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

    TRACK_GENERAL = 1
    TRACK_MACHINE_LEARNING = 2
    TRACK_TOOLS = 3
    TRACK_DOMAIN_ONLY = 4
    
    TOPIC_TRACKS = [
        (TRACK_GENERAL, "General"),
        (TRACK_MACHINE_LEARNING, "Machine Learning"),
        (TRACK_TOOLS, "Tools for Reproducibility"),
        (TRACK_DOMAIN_ONLY, "None, only submit to Domain Symposia"),
    ]

    DOMAIN_NONE = 1
    DOMAIN_MEDICAL_IMAGING = 2
    DOMAIN_METEOROLOGY = 3
    DOMAIN_ASTRONOMY = 4
    DOMAIN_BIO_INFORMATICS = 5
    
    DOMAIN_SYMPOSIA = [
        (DOMAIN_NONE, "None, only submit to tracks"),
        (DOMAIN_MEDICAL_IMAGING, "Medical imaging"),
        (DOMAIN_METEOROLOGY, "Meteorology, climatology, and atmospheric and oceanic science"),
        (DOMAIN_ASTRONOMY, "Astronomy and astrophysics"),
        (DOMAIN_BIO_INFORMATICS, "Bio-informatics"),
    ]

    submission_type = models.IntegerField(choices=SUBMISSION_TYPES, default=1)
    topic_track = models.IntegerField(choices=TOPIC_TRACKS, default=1)
    domain_symposium = models.IntegerField(choices=DOMAIN_SYMPOSIA, default=1)

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
    
    track = models.IntegerField(choices=TRACKS)

    package_list = models.TextField(
        "Package List",
        help_text="""A list of Python packages that attendees will need to
have installed prior to the class to follow along. Please mention if
any packages are not cross platform. Installation instructions or
links to installation documentation should be provided for packages
that are not available through easy_install, pip, EPD, Anaconda CE
etc., or that require third party libraries."""
    )

    class Meta:
        verbose_name = "tutorial proposal"


class BofProposal(ProposalBase):
    class Meta:
        verbose_name = "birds of a feather proposal"


class SprintProposal(ProposalBase):
    class Meta:
        verbose_name = "sprint proposal"
