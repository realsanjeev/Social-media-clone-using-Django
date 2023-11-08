from django.contrib import admin
from posts.models import Post, LikePost, CommentPost

# Register your models here.
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(CommentPost)