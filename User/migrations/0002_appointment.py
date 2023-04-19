# Generated by Django 4.0.2 on 2023-04-18 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.doctor')),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.patient')),
            ],
        ),
    ]
