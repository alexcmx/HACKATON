# Generated by Django 2.0.13 on 2019-04-06 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20190407_0207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestclient',
            name='pin',
        ),
    ]