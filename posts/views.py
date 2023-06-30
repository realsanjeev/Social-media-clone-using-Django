from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Home is working..</h1>")

def posts(request):
    return HttpResponse("<h2>Posts is working..</h2>")