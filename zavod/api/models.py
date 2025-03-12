from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    username = models.CharField(max_length=255, blank=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
class Tags(models.Model):
    tag = models.CharField(max_length=100)

class News(models.Model):
    title = models.CharField(max_length=300, unique=True)
    text = models.TextField(blank=False)
    picture = models.ImageField(blank=False)
    tag = models.ManyToManyField(Tags, blank=True)
    views = models.BigIntegerField(default=0)