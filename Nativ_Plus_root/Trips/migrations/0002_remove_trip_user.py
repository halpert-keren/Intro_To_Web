# Generated by Django 3.0.6 on 2020-07-19 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trips', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='user',
        ),
    ]
