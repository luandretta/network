from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    """
    Post Model including autor and time
    Like and dislike posts
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    posted_on = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True,
                                      related_name='dislikes')


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
                                  default='static/images/user.png',
                                  blank=True)
    bg_pic = CloudinaryField('Background Picture',
                             default='static/images/bg.png',
                             blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    followers = models.ManyToManyField(User, blank=True,
                                       related_name='followers')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Once the User is saved in the database, the profile object will be created
    Create the instance
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Save the instance object (profile)
    """
    instance.profile.save()
