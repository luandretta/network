from django.urls import path
from .views import (
    AllPostsListView, PostDetailView, PostEditView, PostDeleteView,
    CommentDeleteView, ProfileView, ProfileEditView, AddFollower,
    RemoveFollower, LikePost, Dislike, UserSearch, FollowingPostsListView,
    ListFollowers)


urlpatterns = [
     path('', AllPostsListView.as_view(), name='post-list'),
     path('feed/', FollowingPostsListView.as_view(), name='feed'),
     path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
     path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
     path('post/delete/<int:pk>/', PostDeleteView.as_view(),
          name='post-delete'),
     path('post/<int:post_pk>/comment/delete<int:pk>/',
          CommentDeleteView.as_view(), name='comment-delete'),
     path('post/<int:pk>/like/', LikePost.as_view(), name='post-like'),
     path('post/<int:pk>/dislike/', Dislike.as_view(), name='dislike'),
     path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
     path('profile/edit/<int:pk>/', ProfileEditView.as_view(),
          name='profile-edit'),
     path('profile/<int:pk>/followers', ListFollowers.as_view(),
          name='list-followers'),
     path('profile/<int:pk>/followers/add', AddFollower.as_view(),
          name='add-follower'),
     path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(),
          name='remove-follower'),
     path('search/', UserSearch.as_view(), name='profile-search'),
]
