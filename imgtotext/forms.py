from django import forms
from .models import *

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']
        widgets = {'image': forms.FileInput(attrs={'class': 'form-control'})}
