from django.urls import path
from posts import views

urlpatterns = [
    path("", views.home, name="index"),
    path('home', views.home, name="home"),
    path('upload', views.upload_view, name="upload_view"),
    path('explore', views.explore_view, name='explore'),
    path('notifications', views.notification_view, name="notifications"),
    path('search', views.search_user, name="search"),
    path('user/<str:username>', views.user_view, name="user"),
    path('posts', views.posts, name="posts"),
    path('like-post/', views.like_post_view, name="like-post"),

]
