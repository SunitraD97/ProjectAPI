from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return self.name

