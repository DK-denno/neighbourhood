from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Neighbourhoods(models.Model):
    name = models.CharField(max_length=10)
    location =  models.CharField(max_length=10)
    hotlines = models.CharField(max_length=20)
    health = models.CharField(max_length=10)

    def __str__(self):
        return self.name



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

class Businesses(models.Model):
    name = models.CharField(max_length=10)
    details = models.CharField(max_length=100)
    neighbourhood = models.ForeignKey(Neighbourhoods,related_name='businesses')
    
    def __str__(self):
        return self.name