# Generated by Django 3.0.6 on 2020-07-19 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='driver_name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
