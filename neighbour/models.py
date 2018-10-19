from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Neighbourhoods(models.Model):
    name = models.CharField(max_length=10)
    location =  models.CharField(max_length=10)
    details =  models.CharField(max_length=40)
