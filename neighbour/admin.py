from django.contrib import admin
from .models import Profile,Neighbourhoods,Businesses,Message
# Register your models here.

admin.site.register(Profile)
admin.site.register(Neighbourhoods)
admin.site.register(Businesses)
admin.site.register(Message)