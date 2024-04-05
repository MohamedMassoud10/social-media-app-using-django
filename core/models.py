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
    image=models.ImageField(upload_to='post_images')
    caption=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)
    no_of_likes=models.IntegerField(default=0)
    def __str__(self):
        return self.user