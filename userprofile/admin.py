from django.contrib import admin
from .models import Profile, FollowerCount, Contact

# Register your models here.
# class ProfileAdmin(admin.M)
admin.site.register(Profile)
admin.site.register(FollowerCount)

admin.site.register(Contact)
