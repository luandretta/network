from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView


class AllPostsListView(View):
    """
    View from all posts sorted by the latest
    """
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-posted_on')
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'titbit/all_post_list.html', context)

    # Save the new post
    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-posted_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            context = {
                'post_list': posts,
                'form': form,
            }

        return render(request, 'titbit/all_post_list.html', context)


class PostDetailView(View):
    """
    View an individual post in more detail
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
            # messages.add_message(request, messages.SUCCESS, 'Your comment has been submitted')

        comments = Comment.objects.filter(post=post).order_by('-posted_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'titbit/post_detail.html', context)


class PostEditView(UpdateView):
    """
    Edit the post
    Redirect to the previous page through the primary key
    """
    model = Post
    fields = ['content']
    template_name = 'titbit/post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})


class PostDeleteView(DeleteView):
    """
    Delete the post
    Redirect to the previous page through the primary key
    """
    model = Post
    template_name = 'titbit/post_delete.html'
    success_url = reverse_lazy('post-list')


class CommentDeleteView(DeleteView):
    """
    Delete the comment
    Redirect to the post detail
    """
    model = Comment
    template_name = 'titbit/comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})
