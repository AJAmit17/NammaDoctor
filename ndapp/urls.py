from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('services/',views.services, name="services"),
    path('contact/',views.contact, name="contact"),
    path('emergency-guidelines/',views.emergencies, name="emergency-guidelines"),
    path('medical-news/',views.medicalNews, name="medicalnews"),
]
