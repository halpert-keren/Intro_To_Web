# Generated by Django 3.0.6 on 2020-07-19 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trips', '0004_trip_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]