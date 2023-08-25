from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#user registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField(max_length=30, required=True)
    lastname = forms.CharField(max_length=30, required=True)
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
        fields = ['username', 'email', 'password1', 'password2', 'firstname', 'lastname', 'gender', 'contact_number', 'dob']

#user updation form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    firstname = forms.CharField(max_length=30, required=True)
    lastname = forms.CharField(max_length=30, required=True)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)
    contact_number = forms.CharField(max_length=15, required=True,widget=forms.TextInput(attrs={'placeholder': '+91'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    medication_name = forms.CharField(max_length=100, required=False)
    medication_dosage = forms.CharField(max_length=50, required=False)
    medication_frequency = forms.IntegerField(min_value=0)

    allergies = forms.CharField(max_length=200, required=False)
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
    blood_group = forms.ChoiceField(choices=blood_group_choices, required=False)
    previous_surgeries = forms.CharField(required=False)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'firstname', 'lastname',
            'gender', 'contact_number', 'dob',
            'medication_name', 'medication_dosage', 'medication_frequency',
            'allergies', 'blood_group', 'previous_surgeries'
        ]

#profile update form
class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'border border-gray-300 rounded-md p-2'}))
    class Meta:
        model = Profile
        fields = ['image']