# Generated by Django 4.1.10 on 2023-08-18 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remedies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remedies',
            name='author',
        ),
        migrations.RemoveField(
            model_name='remedies',
            name='date_posted',
        ),
    ]
