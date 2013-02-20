from django.db import models

from symposion.proposals.models import ProposalBase


class Proposal(ProposalBase):
    
    AUDIENCE_LEVEL_NOVICE = 1
    AUDIENCE_LEVEL_EXPERIENCED = 2
    AUDIENCE_LEVEL_INTERMEDIATE = 3
    
    AUDIENCE_LEVELS = [
        (AUDIENCE_LEVEL_NOVICE, "Novice"),
        (AUDIENCE_LEVEL_INTERMEDIATE, "Intermediate"),
        (AUDIENCE_LEVEL_EXPERIENCED, "Experienced"),
    ]
    
    audience_level = models.IntegerField(choices=AUDIENCE_LEVELS)
    
    recording_release = models.BooleanField(
        default=True,
        help_text="By submitting your talk proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box."
    )
    
    class Meta:
        abstract = True


class TalkPosterProposal(Proposal):
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
