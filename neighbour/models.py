from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Neighbourhoods(models.Model):
    user = models.ForeignKey(User,related_name='users')
    name = models.CharField(max_length=10)
    location =  models.CharField(max_length=10)
   
   
    def __str__(self):
        return self.name



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    neighbourhood = models.ForeignKey(Neighbourhoods,related_name='users')
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
    user = models.ForeignKey(User,related_name='businesses')
    name = models.CharField(max_length=10)
    dp = models.ImageField(upload_to='biashara')
    details = models.CharField(max_length=100)
    neighbourhood = models.ForeignKey(Neighbourhoods,related_name='businesses')
  
    def __str__(self):
        return self.name

class Message(models.Model):
    message = models.CharField(max_length=1000)
    user = models.ForeignKey(User,related_name='message')
    neighbourhood = models.ForeignKey(Neighbourhoods,related_name='mess')