from django import forms
from .models import Remedies

class RemedyForm(forms.ModelForm):
    class Meta:
        model = Remedies
        fields = ['name', 'description', 'image']
