# Generated by Django 3.0.6 on 2020-07-19 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trips', '0002_auto_20200719_0639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='rating',
        ),
    ]