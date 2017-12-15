from django.db import models

# Create your models here.


class Post(models.Model):
    user = models.CharField(max_length=30)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.user