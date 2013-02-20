from django import forms

from markitup.widgets import MarkItUpWidget

from scipy2013.proposals.models import TalkPosterProposal, TutorialProposal, BofProposal, SprintProposal


class ProposalForm(forms.ModelForm):
    
    def clean_description(self):
        value = self.cleaned_data["description"]
        if len(value) > 400:
            raise forms.ValidationError(
                u"The description must be less than 400 characters"
            )
        return value


class TalkPosterProposalForm(ProposalForm):

    class Meta:
        model = TalkPosterProposal
        fields = [
            "title",
            "audience_level",
            "description",
            "abstract",
            "additional_notes",
            "recording_release",
        ]
        widgets = {
            "abstract": MarkItUpWidget(),
            "additional_notes": MarkItUpWidget(),
        }


class TutorialProposalForm(ProposalForm):

    class Meta:
        model = TutorialProposal
        fields = [
            "title",
            "audience_level",
            "description",
            "abstract",
            "additional_notes",
            "recording_release",

        ]
        widgets = {
            "abstract": MarkItUpWidget(),
            "additional_notes": MarkItUpWidget(),
        }


class BofProposalForm(ProposalForm):

    class Meta:
        model = BofProposal
        fields = [
            "title",
            "description",
            "additional_notes",
        ]
        widgets = {
            "description": forms.widgets.Textarea(attrs={"class": "span9"}),
            "additional_notes": MarkItUpWidget(),
        }


class SprintProposalForm(ProposalForm):

    class Meta:
        model = SprintProposal
        fields = [
            "title",
            "description",
            "additional_notes",
        ]
        widgets = {
            "description": forms.widgets.Textarea(attrs={"class": "span9"}),
            "additional_notes": MarkItUpWidget(),
        }
