# Generated by Django 3.2.18 on 2023-05-02 08:14

import cloudinary.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('titbit', '0006_auto_20230429_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='comment_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bg_pic',
            field=cloudinary.models.CloudinaryField(blank=True, default='static/images/bg.png', max_length=255, verbose_name='Background Picture'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, default='static/images/user.png', max_length=255, verbose_name='Profile Picture'),
        ),
    ]
