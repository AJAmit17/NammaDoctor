from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#user registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)
    contact_number = forms.CharField(max_length=15, required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'gender', 'contact_number', 'dob']

#user updation form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)
    contact_number = forms.CharField(max_length=15, required=True,widget=forms.TextInput(attrs={'placeholder': '+91'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    blood_group_choices = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_group = forms.ChoiceField(choices=blood_group_choices, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'gender', 'contact_number', 'dob','blood_group']

#profile update form
class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'border border-gray-300 rounded-md p-2'}))
    class Meta:
        model = Profile
        fields = ['image']