# Generated by Django 3.2.4 on 2021-06-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0003_auto_20210608_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='assignedDoctorId',
        ),
        migrations.AddField(
            model_name='patient',
            name='assignedDoctor',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
