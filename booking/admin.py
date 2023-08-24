from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'doctor', 'service', 'day', 'time', 'time_ordered']

admin.site.register(Appointment, AppointmentAdmin)