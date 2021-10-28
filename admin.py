from django.contrib import admin
from .models import Post, Likes

admin.site.register(Post, Likes)

# Register your models here.
