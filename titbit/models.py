from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.db.models.signal import post_save
from django.dispatch import receiver


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


class UserProfile(models.Model):
    """
    Profile Model each User can have only one Profile
    """
    user = models.OneToOneField(User,
                                primary_key=True,
                                verbose_name='user',
                                related_name='profile',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=150, blank=True, null=True)
    profile_pic = CloudinaryField('Profile Picture',
                                  default='user.png',
                                  blank=True)
    bg_pic = CloudinaryField('Background Picture',
                              default='bg.png',
                              blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
