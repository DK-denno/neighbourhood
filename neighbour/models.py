from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Neighbourhoods(models.Model):
    user = models.ForeignKey(User,related_name='neighbourhood')
    name = models.CharField(max_length=10)
    admin = models.OneToOneField(User,related_name='admin',null=True)
    location =  models.CharField(max_length=10)
   
   
    def __str__(self):
        return self.name



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    neighbourhood = models.ForeignKey(Neighbourhoods,related_name='users',null=True)
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
    details = models.CharField(max_length=1000)
    neighbourhood = models.ForeignKey(Neighbourhoods,related_name='businesses')
  
    def __str__(self):
        return self.name

class Message(models.Model):
    message = models.CharField(max_length=1000)
    user = models.ForeignKey(User,related_name='message')
    neighbourhood = models.ForeignKey(Neighbourhoods,related_name='mess')

class Comments(models.Model):
    comment = models.CharField(max_length=1000)
    user = models.ForeignKey(User,related_name='commentings',on_delete=models.CASCADE)
    message = models.ForeignKey(Message,related_name='comm')