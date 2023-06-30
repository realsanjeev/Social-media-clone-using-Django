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
        form = MyLoginForm(request, data=request.POST)
        print("************************************")
        if form.is_valid():
            print("````````````````````************************************````````````````````")
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('/home')
            error_message = {"message": "Invalid credential"}

            return render(request, template_file, error_message)
    else:
        form = MyLoginForm()
    context = {"form": form}
    return render(request, template_file, context)

def signup_view(request):
    template_file = os.path.join("user", "signup.html")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            
            form.save()
            user_obj = User.objects.get(username=username)
            print("-"*100, user_obj)
            new_profile = Profile.objects.create(user=user_obj, id_user=user_obj.id)
            new_profile.save()

            return render(request, template_file)
    else:
        form = SignUpForm()
    context = {"form": form}
    return render(request, template_file, context)

def logout_view(request):
    logout(request)
    return redirect('/signin')