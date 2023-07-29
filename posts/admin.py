from django.contrib import admin
from posts.models import Post, LikePost

# Register your models here.
admin.site.register(Post)
admin.site.register(LikePost)