from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

#Registering a new user view page
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
           form.save()
           #username = form.cleaned_data.get('username') 
           messages.success(request, f'Account created successfully!')
           return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'user_regi/register.html', {
        'form': form,
        'title': 'Register'
        })

#updating already exist user details
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your Account has been Updated!')
            return redirect('home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'user_regi/profile.html', {
        'title': 'Profile',
        'user_form': user_form,
        'profile_form': profile_form
    })