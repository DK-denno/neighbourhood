from django.shortcuts import render
from django.contrib.auth import login,authenticate
from .forms import SignUpForm
# Create your views here.

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username,email=email,password=raw_password)
            login(request,user)
    return render(request,'signup.html',{"form":form})





def index(request):
    return render(request,'index.html')
