import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User  # Correct import for User model

# Create your models here.
class Post(models.Model):  
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    post_img = models.ImageField(upload_to='post_images')
    caption = models.TextField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

class LikePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    username = models.ForeignKey(User, on_delete=models.CASCADE, to_field="username")

class CommentPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, to_field="id")  
    username = models.ForeignKey(User, on_delete=models.CASCADE, to_field="username")
    comment = models.TextField(null=True)
