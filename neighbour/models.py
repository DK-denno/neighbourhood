from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

class Neighbourhoods(models.Model):
    user = models.ForeignKey(User,related_name='neighbourhood')
    name = models.CharField(max_length=10)
    admin = models.OneToOneField(User,related_name='admin',null=True)
    locale = models.CharField(max_length=20)
   
    
    def __str__(self):
        return self.neighbourhood_name

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood_by_id(cls, id):
        neighbourhoods = cls.objects.filter(pk=id)
        neighbourhoods.delete()

    @classmethod
    def get_neighbourhood_by_id(cls, id):
        neighbourhoods = cls.objects.get(pk=id)
        return neighbourhoods

    @classmethod
    def filter_by_location(cls, location):
        neighbourhoods = cls.objects.filter(location=location)
        return neighbourhoods

    @classmethod
    def search_neighbourhood(cls, search_term):
        neighbourhoods = cls.objects.filter(neighbourhood_name__icontains=search_term)
        return neighbourhoods

    @classmethod
    def update_neighbourhood(cls, id):
        neighbourhoods = cls.objects.filter(id=id).update(id=id)
        return neighbourhoods

    @classmethod
    def update_neighbourhood(cls, id):
        neighbourhoods = cls.objects.filter(id=id).update(id=id)
        return neighbourhoods
   
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

    def __str__(self):
        return self.business_name


    def save_business(self):
        self.save()

    @classmethod
    def delete_business_by_id(cls, id):
        businesses = cls.objects.filter(pk=id)
        businesses.delete()

    @classmethod
    def get_businesses_by_id(cls, id):
        businesses = cls.objects.get(pk=id)
        return businesses

    @classmethod
    def filter_by_location(cls, location):
        businesses = cls.objects.filter(location=location)
        return businesses

    @classmethod
    def search_businesses(cls, search_term):
        businesses = cls.objects.filter(business_name__icontains=search_term)
        return businesses

    @classmethod
    def update_business(cls, id):
        businesses = cls.objects.filter(id=id).update(id=id)
        return businesses

    @classmethod
    def update_business(cls, id):
        businesses = cls.objects.filter(id=id).update(id=id)
        return businesses

class Comments(models.Model):
    comment = models.CharField(max_length=1000)
    user = models.ForeignKey(User,related_name='commentings',on_delete=models.CASCADE)
    message = models.ForeignKey(Message,related_name='comm')

    def save_comment(self):
        self.save()

    def get_comment(self, id):
        comments = Review.objects.filter(image_id=id)
        return comments

    def __str__(self):
        return self.comment