from django.db import models


class Post(models.Model):  
    name = models.CharField(max_length=50)
    status = models.TextField()
    image = models.FileField(upload_to='postimage/%y/%m/%d',blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return self.name