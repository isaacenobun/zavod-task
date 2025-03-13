from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Tags(models.Model):
    tag = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tag

class News(models.Model):
    title = models.CharField(max_length=300, unique=True)
    text = models.TextField(blank=False)
    picture = models.ImageField(upload_to='images/')
    tag = models.ManyToManyField(Tags, blank=True)
    views = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.BigIntegerField(default=0)
    
    def __str__(self):
        
        return self.title

class User(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    username = models.CharField(max_length=255, blank=False)
    likes = models.ManyToManyField(News, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']