from django import forms

from markitup.widgets import MarkItUpWidget

from scipyla2016.proposals.models import (TalkPosterProposal, TutorialProposal, BofProposal, SprintProposal)


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
            "description",
            "abstract",
            "submission_type",
            "topic_track",
            "domain_symposium",
            "additional_notes",
        ]
        widgets = {
            "abstract": MarkItUpWidget(),
            "description": forms.widgets.Textarea(attrs={"class": "span9"}),
            "additional_notes": MarkItUpWidget(),
        }


class TutorialProposalForm(ProposalForm):

    class Meta:
        model = TutorialProposal
        fields = [
            "title",
            "track",
            "description",
            "abstract",
            "package_list",
            "additional_notes",

        ]
        widgets = {
            "abstract": MarkItUpWidget(),
            "additional_notes": MarkItUpWidget(),
            "description": forms.widgets.Textarea(attrs={"class": "span9"}),
            "package_list": forms.widgets.Textarea(attrs={"class": "span9"}),
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
