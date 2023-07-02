import uuid
from datetime import datetime
from django.db import models


# Create your models here.
class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    user = models.CharField(max_length=100)
    post_img = models.ImageField(upload_to='post_images')
    caption = models.TextField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now())

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
