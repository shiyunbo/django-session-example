from django import forms
from .models import InvitationCode


class InvitationCodeForm(forms.ModelForm):
    class Meta:
        model = InvitationCode
        fields = ("code",)
