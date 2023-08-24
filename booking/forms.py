from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'service', 'day', 'time']

class AdminUsernameForm(forms.Form):
    admin_username = forms.CharField(label='Admin Username', max_length=100)
