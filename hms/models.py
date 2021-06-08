from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


departments=[('Cardiologist','Cardiologist'),
('Dermatologist','Dermatologist'),
('Emergency Medicine Specialist','Emergency Medicine Specialist'),
('Allergist/Immunologist','Allergist/Immunologist'),
('Anesthesiologist','Anesthesiologist'),
('Colon and Rectal Surgeon','Colon and Rectal Surgeon')
]
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50, default='user')
    profile_pic= models.ImageField(upload_to='profile_photos/Doctor/', default='profile_photos/Doctor/default_ku6ks9.jpg')
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    
    @receiver(post_save, sender=User)
    def create_doctor_profile(sender, instance, created, **kwargs):
      if created:
          Doctor.objects.create(user=instance)
  
    @receiver(post_save, sender=User)
    def save_doctor_profile(sender, instance, created=False, **kwargs):
      instance.doctor.save()

    def save_doctor(self):
      self.save()

    def delete_doctor(self):
      self.delete() 
    
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
      
    @property
    def get_id(self):
        return self.user.id
      
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)

