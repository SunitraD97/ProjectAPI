from rest_framework import viewsets
from .serializers import PostSerializer,CommentSerializer,UserSerializer
#from .models import BlogPost
from ProjectAPI.blog.post.models import Post
from ProjectAPI.blog.comment.models import Comment
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response

# class BlogPostViewSet(viewsets.ModelViewSet):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def delete(self, request, format=None):
        ...

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    # def get(self, request, format=None):
    #     post = Post.objects.all()
    #     serializer = PostSerializer(post, many=True)
    #     return Response(serializer.url)
    # def post(self, request, format=None):
    #     ...
    #     #logic for HTTP POST operation
    def delete(self, request, format=None):
        ...

    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def delete(self, request, format=None):
        ...
  