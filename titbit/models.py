from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    """
    Post Model including autor and time
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    posted_on = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    """
    Comment Model including autor and time
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    posted_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)