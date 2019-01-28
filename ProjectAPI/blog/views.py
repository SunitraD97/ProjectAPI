from rest_framework import viewsets
from .serializers import BlogPostSerializer,PostSerializer,CommentSerializer
from .models import BlogPost
from ProjectAPI.blog.post.models import Post
from ProjectAPI.blog.comment.models import Comment
from rest_framework.views import APIView
from rest_framework.response import Response

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    
 

    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
