from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminder_list, name='reminder_list'),
    path('create/', views.reminder_create, name='reminder_create'),
    path('<int:pk>/', views.reminder_detail, name='reminder_detail'),
    path('<int:pk>/update/', views.reminder_update, name='reminder_update'),
    path('<int:pk>/delete/', views.reminder_delete, name='reminder_delete'),
]
