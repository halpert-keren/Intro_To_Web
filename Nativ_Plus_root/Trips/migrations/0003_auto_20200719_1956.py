# Generated by Django 3.0.6 on 2020-07-19 16:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Trips', '0002_auto_20200719_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='users',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
