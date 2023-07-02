from django.contrib import admin
from posts.models import Posts, LikePost

# Register your models here.
admin.site.register(Posts)
admin.site.register(LikePost)