# Generated by Django 4.2 on 2023-06-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_regi', '0002_userprofile_date_of_birth_userprofile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]