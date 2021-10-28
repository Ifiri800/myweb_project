from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import  Post, Likes


class PostSeriazlizer(serializers.ModelSerializer):
    class meta:
        model = Post
        fields = (
            "create_at", "created_by", "content"
        )


class LikestSerializer(serializers.ModelSerializer):
    class meta:
        model = Likes
        fields = (
            "create_at", "created_by", "content" 'likes'
        )


      