from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Remedies(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='remedy_images/')
    

    def __str__(self):
        return self.name
