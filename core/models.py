from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User =get_user_model()

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    profileimag=models.ImageField(upload_to='profile_images/%y/%m/%d',default='blank_profile_pic.png')
    location=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.user.username
