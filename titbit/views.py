from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .models import Post, Comment, UserProfile, Notification
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
from django.core.paginator import Paginator


class AllPostsListView(LoginRequiredMixin, View):
    """
    View from all posts sorted by the latest
    Create new post using post form
    """
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-posted_on')
        form = PostForm()

        paginator = Paginator(posts, 4)
        page_num = request.GET.get('page')
        posts = paginator.get_page(page_num)

        context = {
            'post_list': posts,
            'form': form,
            'page_num': page_num,
        }

        return render(request, 'titbit/all_post_list.html', context)

    # Save the new post
    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-posted_on')
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            context = {
                'post_list': posts,
                'form': form,
            }

        return render(request, 'titbit/all_post_list.html', context)


class FollowingPostsListView(LoginRequiredMixin, View):
    """
    Displays only posts from people who user is following and from user
    Create new post using post form
    """
    def get(self, request, *args, **kwargs):
        logged_in_user = request.user
        following_posts = Post.objects.filter(
            Q(author__profile__followers__in=[logged_in_user.id]) |
            Q(author=request.user)
        ).order_by('-posted_on')
        form = PostForm()

        paginator = Paginator(following_posts, 4)
        page_num = request.GET.get('page')
        following_posts = paginator.get_page(page_num)

        context = {
            'following_post_list': following_posts,
            'form': form,
            'page_num': page_num,
        }

        return render(request, 'titbit/feed.html', context)

    # Save the new post
    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-posted_on')
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        return redirect('feed')


class PostDetailView(LoginRequiredMixin, View):
    """
    View an individual post in more detail
    View the comments of this post
    User can comment this post 
    Create Notification type 2 (Comment)
    """
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()

        comments = Comment.objects.filter(post=post).order_by('-posted_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'titbit/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            # messages.add_message(request, messages.SUCCESS,
            # 'Your comment has been submitted')

        comments = Comment.objects.filter(post=post).order_by('-posted_on')

        notification = Notification.objects.create(notification_type=2,
                                                   from_user=request.user,
                                                   to_user=post.author,
                                                   post=post)

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'titbit/post_detail.html', context)


class CommentReplyView(LoginRequiredMixin, View):
    """
    Reply a comment
    Create Notification type 2 (comment)
    """
    def post(self, request, post_pk, pk, *args, **kwargs):
        post = Post.objects.get(pk=post_pk)
        parent_comment = Comment.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.parent = parent_comment
            new_comment.save()

        notification = Notification.objects.create(notification_type=2,
                                                   from_user=request.user,
                                                   to_user=parent_comment.author,
                                                   comment=new_comment)

        return redirect('post-detail', pk=post_pk)


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit the post
    Redirect to the previous page through the primary key
    Boolean expression to UserPassesTextMixin
    """
    model = Post
    fields = ['content', 'image']
    template_name = 'titbit/post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class CommentEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit the comment
    Redirect to the previous page through the primary key
    Boolean expression to UserPassesTextMixin
    """
    model = Comment
    fields = ['comment']
    template_name = 'titbit/comment_edit.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete the post
    Redirect to the previous page through the primary key
    Boolean expression to UserPassesTextMixin
    """
    model = Post
    template_name = 'titbit/post_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete the comment
    Redirect to the post detail
    Boolean expression to UserPassesTextMixin
    """
    model = Comment
    template_name = 'titbit/comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser


class ProfileView(LoginRequiredMixin, View):
    """
    View from User's Profile
    Each Profile has a unique url through pk
    Displays posts and followers from User
    """
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-posted_on')

        paginator = Paginator(posts, 4)
        page_num = request.GET.get('page')
        posts = paginator.get_page(page_num)

        followers = profile.followers.all()

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        number_of_followers = len(followers)

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'number_of_followers': number_of_followers,
            'is_following': is_following,
            'page_num': page_num,
        }

        return render(request, 'titbit/profile.html', context)


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit the own profile
    """
    model = UserProfile
    fields = ['name', 'profile_pic', 'bg_pic', 'bio', 'birth_date', 'location']
    template_name = 'titbit/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


class AddFollower(LoginRequiredMixin, View):
    """
    Follow another User
    Notification type 3 (Follow)
    """
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user)

        notification = Notification.objects.create(notification_type=3,
                                                   from_user=request.user,
                                                   to_user=profile.user)

        return redirect('profile', pk=profile.pk)


class RemoveFollower(LoginRequiredMixin, View):
    """
    Unfollow an User
    """
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect('profile', pk=profile.pk)


class LikePost(LoginRequiredMixin, View):
    """
    Like posts
    Users cannot like and dislike the same post
    Notification type 1 (Like)
    """
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)
            notification = Notification.objects.create(notification_type=1,
                                                       from_user=request.user,
                                                       to_user=post.author,
                                                       post=post)

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class Dislike(LoginRequiredMixin, View):
    """
    Dislike posts
    Users cannot like and dislike the same post
    """
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class LikeComment(LoginRequiredMixin, View):
    """
    Like comment
    Users cannot like and dislike the same comment
    """
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        is_dislike = False

        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            comment.dislikes.remove(request.user)

        is_like = False

        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            comment.likes.add(request.user)
            notification = Notification.objects.create(notification_type=1,
                                                       from_user=request.user,
                                                       to_user=comment.author,
                                                       comment=comment)

        if is_like:
            comment.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class DislikeComment(LoginRequiredMixin, View):
    """
    Dislike comment
    Users cannot like and dislike the same comment
    """
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        is_like = False

        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            comment.likes.remove(request.user)

        is_dislike = False

        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            comment.dislikes.add(request.user)

        if is_dislike:
            comment.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class UserSearch(View):
    """
    Search users
    """
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = UserProfile.objects.filter(
            Q(user__username__icontains=query)
        )

        context = {
            'profile_list': profile_list,
        }

        return render(request, 'titbit/search.html', context)


class ListFollowers(View):
    """
    Display the followers list
    """
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        followers = profile.followers.all()

        paginator = Paginator(followers, 2)
        page_num = request.GET.get('page')
        followers = paginator.get_page(page_num)

        context = {
            'profile': profile,
            'followers': followers,
            'page_num': page_num,
        }

        return render(request, 'titbit/followers_list.html', context)


class PostNotification(View):
    """
    Display the notifications
    """
    def get(self, request, notification_pk, post_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)
        post = Post.objects.get(pk=post_pk)

        notification.user_has_seen = True
        notification.save()

        return redirect('post-detail', pk=post_pk)


class FollowNotification(View):
    """
    Notifications for when someone follows you
    """
    def get(self, request, notification_pk, profile_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)
        profile = UserProfile.objects.get(pk=profile_pk)

        notification.user_has_seen = True
        notification.save()

        return redirect('profile', pk=profile_pk)


class RemoveNotification(View):
    """
    Remove the notifications when user has seen
    """
    def delete(self, request, notification_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)

        notification.user_has_seen = True
        notification.save()

        return HttpResponse('Success', content_type='text/plain')
