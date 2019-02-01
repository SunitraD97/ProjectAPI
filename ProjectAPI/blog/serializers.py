from rest_framework import serializers
from django.contrib.auth.models import User
# from .models import BlogPost
from ProjectAPI.blog.post.models import Post
from ProjectAPI.blog.comment.models import Comment


# class BlogPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BlogPost
#         fields = ('url','title','content','timestamp')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('url','title','user','status','image','timestamp')
      
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('url','user','comment','timestamp')
      