from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):  
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.TextField()
    image = models.FileField(upload_to='postimage/%y/%m/%d',blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
       return self.title

