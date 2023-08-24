from django.urls import path
from .views import remedy_list,add_remedy

urlpatterns = [
    path('',remedy_list,name='remedy_list'),
    path('add/',add_remedy, name='add_remedy'),
]
