from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    class Meta:
        model = User
        exclude = []
        fields = ['first_name','last_name','username','email','password1','password2']