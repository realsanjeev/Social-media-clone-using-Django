from django.urls import path, include
from userprofile import views

urlpatterns = [
    path('login', views.login_view, name="login"),
    path('signup', views.signup_view, name="signup"),
    path('logout', views.logout_view, name="logout"),
    path('settings', views.settings, name="account_setting"),
    path('profile', views.profile, name="profile"),
]
