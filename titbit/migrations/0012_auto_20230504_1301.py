# Generated by Django 3.2.18 on 2023-05-04 13:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titbit', '0011_auto_20230504_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bg_pic',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
