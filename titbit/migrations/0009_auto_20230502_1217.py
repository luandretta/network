# Generated by Django 3.2.18 on 2023-05-02 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titbit', '0008_auto_20230502_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bg_pic',
            field=models.ImageField(blank=True, default='images/bg.png', upload_to='', verbose_name='Background Picture'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/user.png', upload_to='', verbose_name='Profile Picture'),
        ),
    ]
