from django.urls import path
from . import views
from .views import doc_list

urlpatterns = [
    path('', doc_list, name='doctors_list'),
    path('results/', views.doc_result, name='doc_result'),
    path('register/', views.doc_regi, name='doc_regi'),
    path('maps/', views.doc_loc, name='doc_loc'),
]
