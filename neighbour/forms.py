from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Neighbourhoods

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)

    class Meta:
        model = User
        exclude = []
        fields = ['first_name','last_name','username','email','password1','password2']

class NeighbourhoodsForm(forms.ModelForm):
    class Meta:
        model = Neighbourhoods
        exclude = []
        fields = ['name','location','hotlines','health']