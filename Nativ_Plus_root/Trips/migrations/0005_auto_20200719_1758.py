# Generated by Django 3.0.6 on 2020-07-19 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trips', '0004_auto_20200719_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='user',
            new_name='users',
        ),
    ]