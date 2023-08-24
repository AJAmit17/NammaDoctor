from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField()
    address = models.CharField(max_length=255, default='No address provided')

    def __str__(self):
        return self.name
