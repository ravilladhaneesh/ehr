# Generated by Django 4.0.2 on 2023-04-19 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='patient_name',
        ),
    ]