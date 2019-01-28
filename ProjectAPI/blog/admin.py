from django.contrib import admin
from.models import  BlogPost
from ProjectAPI.blog.post.models import Post
from ProjectAPI.blog.comment.models import Comment

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Post)
admin.site.register(Comment)