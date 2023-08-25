from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('services/',views.services, name="services"),
    path('contact/',views.contact, name="contact"),
    path('emergency-guidelines/',views.emergencies, name="emergency-guidelines"),
    path('medical-news/',views.medicalNews, name="medicalnews"),
    path('health-topics/',views.healthtopics, name="healthtopics"),
    path('terms-and-conditions/',views.termsandconditions, name="tandc"),
    path('privacy-policy/',views.privacypolicy, name="pp"),
    path('privacy-policy/',views.privacypolicy, name="pp"),
    path('locate-on-map/',views.locatedoc, name="locatedoc"),
]
