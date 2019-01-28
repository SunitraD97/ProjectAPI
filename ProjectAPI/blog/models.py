from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField()


    def __str__(self):
        return self.title
