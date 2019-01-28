from rest_framework import serializers
from .models import BlogPost
from ProjectAPI.blog.post.models import Post
from ProjectAPI.blog.comment.models import Comment


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('url','title','content','timestamp')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('url','name','status','image','timestamp')
      
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('url','name','comment','timestamp')
      