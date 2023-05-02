# Generated by Django 3.2.18 on 2023-05-02 09:04

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('titbit', '0007_auto_20230502_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='titbit.comment'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bg_pic',
            field=cloudinary.models.CloudinaryField(blank=True, default='images/bg.png', max_length=255, verbose_name='Background Picture'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, default='images/user.png', max_length=255, verbose_name='Profile Picture'),
        ),
    ]