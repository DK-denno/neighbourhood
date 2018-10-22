from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import SignUpForm,NeighbourhoodsForm,ProfileForm
from .models import Profile
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
            profile = Profile(user=user)
            profile.save()
            login(request,user)
    return render(request,'signup.html',{"form":form})

def index(request):
    form = NeighbourhoodsForm()
    if request.method == 'POST':
        form = NeighbourhoodsForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            return redirect('/')
    return render(request,'index.html',{"form":form})

def profile(request):
        form = ProfileForm()
        current_user=request.user
        profile = Profile.objects.get(user=current_user)
        if request.method == 'POST':
                form = ProfileForm(request.POST,request.FILES,instance=profile)
                if form.is_valid():
                    form.save()
                    return redirect('profile')
                else:
                    message = 'Fill in the form appropriately'
                    return render(request,'profile/profile.html',{"profile":profile,"form":form,"message":message})
        return render(request,'profile/profile.html',{"form":form,"profile":profile})

 