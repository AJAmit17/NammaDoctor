from django.urls import path
from .views import register
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'user_regi/login.html',extra_context = {'title':'Login'}),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'user_regi/logout.html',extra_context = {'title':'Logout'}),name='logout'),
    path('profile/',user_views.profile,name='user-profile'),
     path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='user_regi/password_reset.html',extra_context = {'title':'Password reset'}
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='user_regi/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='user_regi/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='user_regi/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]