from django.urls import path
from posts import views

urlpatterns = [
    path("", views.home, name="index"),
    path('home', views.home, name="home"),
    path('upload', views.upload_view, name="upload_view"),
    path('posts', views.posts, name="posts"),

]
