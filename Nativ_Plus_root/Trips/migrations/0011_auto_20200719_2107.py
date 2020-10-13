# Generated by Django 3.0.6 on 2020-07-19 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Trips', '0010_trip_driver_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='driver_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver', to=settings.AUTH_USER_MODEL),
        ),
    ]
