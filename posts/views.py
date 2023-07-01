import os
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
login_required(login_url="login")
def home(request):
    template_files = os.path.join("posts", "home.html")
    return render(request, template_files)

@login_required(login_url="login")
def posts(request):
    template_files = os.path.join("posts", "home.html")
    return render(request, template_files)

@login_required(login_url='login')
def upload_view(request):
    template_files = os.path.join('posts',  'upload.html')
    if request.method == 'POST':
        pass
    return render(request, template_files)