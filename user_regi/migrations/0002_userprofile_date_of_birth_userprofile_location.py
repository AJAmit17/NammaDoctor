# Generated by Django 4.2 on 2023-06-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_regi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
