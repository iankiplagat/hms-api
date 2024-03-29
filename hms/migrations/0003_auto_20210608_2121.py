# Generated by Django 3.2.4 on 2021-06-08 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hms', '0002_doctor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(default='doctor', max_length=50),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='patient', max_length=50)),
                ('profile_pic', models.ImageField(default='profile_photos/Patient/default_olh4qq.jpg', upload_to='profile_photos/Doctor/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('symptoms', models.CharField(max_length=100)),
                ('assignedDoctorId', models.PositiveIntegerField(null=True)),
                ('admitDate', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
