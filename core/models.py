from django.db import models
from django.contrib.auth import get_user_model
import uuid

from datetime import datetime
# Create your models here.

User =get_user_model()

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    profileimag=models.ImageField(upload_to='profile_images/%y/%m/%d',default='blank_profile_pic.png')
    location=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=50)
    image=models.ImageField(upload_to='post_images',blank=True, null=True)
    caption=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)
    no_of_likes=models.IntegerField(default=0)
    def __str__(self):
        return self.user

class LikePost(models.Model):
    liked_post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return f"Liked by {self.username} on {self.liked_post}"


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    text = models.TextField()
    created_at=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"    