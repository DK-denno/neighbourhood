from django.contrib import admin
from .models import Profile,Neighbourhoods,Hotlines,Businesses
# Register your models here.

admin.site.register(Profile)
admin.site.register(Neighbourhoods)
admin.site.register(Hotlines)
admin.site.register(Businesses)