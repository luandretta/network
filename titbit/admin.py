from django.contrib import admin
from .models import Post, UserProfile, Comment
from django.contrib.auth.models import Group, User

# Unregister Groups
admin.site.unregister(Group)

# Register Posts
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)
