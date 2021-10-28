from django.db.models.aggregates import Count
from rest_framework import views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken import views
from rest_framework.permissions import IsAuthenticated
from .serializers import Post, Likes, PostSerislizer, LikesSerializer

class UserView(APIView, views):
    permission_classes = (IsAuthenticated)

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerislizer(qs, many=True)
        serializer = LikesSerializer
        return Response(qs)
    
    def post(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        if Likes.objects.filter(post=post,created_by=request.user).exists():
            Likes.objects.filter(IsAuthenticated, created_by=request.user).delect()
        elif Likes.objects.filter(like_post=post_id).aggregate(Count('pk')):
         Likes.objects.create(post=post, created_by=request.user)
        return Response
           
        
            