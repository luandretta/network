from django.shortcuts import render
from django.views import View
from .models import Post


class AllPostsListView(View):
    """
    View from all posts sorted by the latest
    """
    def get (self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')

        context = {
            'post_list': posts,
        }

        return render(request, 'titbit/all_post_list.html', context)

