# Generated by Django 3.0.6 on 2020-07-19 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trips', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='passengers',
            field=models.IntegerField(),
        ),
    ]
