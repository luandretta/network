from django.urls import path
from .views import AllPostsListView


urlpatterns = [
    path('', AllPostsListView.as_view(), name='post-list'),
]