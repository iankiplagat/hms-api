# Generated by Django 3.2.4 on 2021-06-08 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0004_auto_20210608_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='assignedDoctor',
            new_name='assignedDoctorId',
        ),
    ]
