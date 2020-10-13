# Generated by Django 3.0.6 on 2020-07-19 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('CurrentLocation', models.CharField(max_length=60)),
                ('Destination', models.CharField(max_length=60)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('passengers', models.IntegerField()),
                ('smoking', models.BooleanField()),
                ('pets', models.BooleanField()),
                ('music', models.BooleanField()),
                ('rating', models.FloatField(default=0)),
            ],
        ),
    ]
