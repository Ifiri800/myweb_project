from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=150)
    content = models.TextField(blank=True)


    class Meta:
        ordering = ('-created_at' ,)

class Likes(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    likes = models.ManyToManyField('self', User, blank=True, name='likes')


    def __str__(self):
        return self.likes


