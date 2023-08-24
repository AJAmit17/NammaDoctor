from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#user registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField(max_length=30, required=True)
    lastname = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'firstname', 'lastname']

#user updation form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']

#profile update form
class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'border border-gray-300 rounded-md p-2'}))
    class Meta:
        model = Profile
        fields = ['image']