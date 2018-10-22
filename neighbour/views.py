from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import SignUpForm,NeighbourhoodsForm,ProfileForm,ChangeNeighbourhood,MessageForm
from .models import Profile,Neighbourhoods,Message,Businesses
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
            return redirect('index')
    return render(request,'signup.html',{"form":form})

def index(request):
    businesses = Businesses.objects.filter(neighbourhood=request.user.profile.neighbourhood)
    print(businesses)
    form = NeighbourhoodsForm()
    message_form = MessageForm()
    if request.method == 'POST':
        form = NeighbourhoodsForm(request.POST)
        message_form = MessageForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            return redirect('/')
        if message_form.is_valid():
            messaging = message_form.save(commit=False)
            print('x')
            messaging.user = request.user
            messaging.neighbourhood = request.user.profile.neighbourhood
            messaging.save()
            return redirect('/')
    messages = Message.objects.filter(neighbourhood=request.user.profile.neighbourhood)
    if request.user.neighbourhood == None:
        message = 'PLEASE CLICK ON THE PROFILES OPTION AND CHOOSE A NEIGHBOURHOOD'
        return render(request,'index.html',{ 'businesses':businesses,"habari":message, "form":form,'message_form':message_form,"messages":messages})
    return render(request,'index.html',{ 'businesses':businesses,"form":form,'message_form':message_form,"messages":messages})
def profile(request):
        form = ProfileForm()
        current_user=request.user
        neighbourhood = ChangeNeighbourhood()
        profile = Profile.objects.get(user=current_user)
        if request.method == 'POST':
                form = ProfileForm(request.POST,request.FILES,instance=profile)
                neighbourhood = ChangeNeighbourhood(request.POST,instance=profile)
                if form.is_valid():
                    form.save()
                    return redirect('profile')
                if neighbourhood.is_valid():
                    neighbourhood.save()
                    return redirect('profile')
                else:
                    message = 'Fill in the form appropriately'
                    return render(request,'profile/profile.html',{"neighbourhood":neighbourhood, "profile":profile,"form":form,"message":message})
        return render(request,'profile/profile.html',{"form":form,"neighbourhood":neighbourhood, "profile":profile})

def profiles(request,id):
    prof = Profile.objects.get(id=id)
    business = Businesses.objects.filter(user=prof.user)
    return render(request,'profile/profiles.html',{"profile":prof})