from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Neighbourhoods(models.Model):
    name = models.CharField(max_length=10)
    location =  models.CharField(max_length=10)
    details =  models.CharField(max_length=40)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    dp =  models.ImageField(upload_to='images')
    bio = models.CharField(max_length=500)
    phone_number = models.BigIntegerField(null=True)
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.user.username
