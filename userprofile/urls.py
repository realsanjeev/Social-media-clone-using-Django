from django.urls import path, include
from userprofile import views

urlpatterns = [
    path('login', views.login_view, name="login"),
    path('signup', views.signup_view, name="signup"),
    path('logout', views.logout_view, name="logout"),
    path('settings', views.settings, name="account_setting"),
    path('profile', views.profile, name="profile"),
    path('follow', views.follow_user, name="follow"),

    path('about', views.about_view, name='about'),
    path('faq', views.faq_view, name='faq'),
    path('features', views.features_view, name='features'),
    path('contacts', views.contact_view, name='contacts'),
]
