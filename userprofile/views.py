import os
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

from userprofile.models import Profile
from userprofile.forms import MyLoginForm, SignUpForm

# Create your views here.
def index(request):
    template_file = os.path.join("user", "base.html")
    return render(request, template_file)

def login_view(request):
    template_file = os.path.join("user", "signin.html")
    if request.method == "POST":
        form = MyLoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

            return render(request, template_file)
    else:
        form = MyLoginForm()
        print(form)
        context = {"form": form}
        return render(request, template_file, context)

def signup_view(request):
    template_file = os.path.join("user", "signup.html")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            print("-"*100)
            form.save()
            user_obj = User.objects.get(username=username)
            profile_obj = Profile.objects.create()
            return render(request, template_file)
    else:
        form = SignUpForm()
    context = {"form": form}
    return render(request, template_file, context)

def logout_view(request):
    logout(request)
    return redirect('/signin')