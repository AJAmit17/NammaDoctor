from django.urls import path
from . import views

urlpatterns = [
    path('', views.medicine_list, name='medicine_list'),
    path('<int:medicine_id>/', views.medicine_detail, name='medicine_detail'),
    path('cart/', views.view_cart, name='view_cart'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_success/', views.order_successful, name='order_success'),
]
