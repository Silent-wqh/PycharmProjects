from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """博客系统"""
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """字符串返回"""
        return f'{self.title}'
