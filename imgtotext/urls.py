from django.urls import path
from .views import ImageToTextView

urlpatterns = [
    path('', ImageToTextView.as_view(), name='image_to_text'),
]
