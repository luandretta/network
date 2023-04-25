from django.urls import path
from .views import AllPostsListView, PostDetailView


urlpatterns = [
    path('', AllPostsListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
