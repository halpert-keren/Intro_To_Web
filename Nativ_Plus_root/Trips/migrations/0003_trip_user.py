# Generated by Django 3.0.6 on 2020-07-19 12:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Trips', '0002_auto_20200719_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
