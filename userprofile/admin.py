from django.contrib import admin
from userprofile.models import Profile, FollowerCount

# Register your models here.
admin.site.register(Profile)
admin.site.register(FollowerCount)