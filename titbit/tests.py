from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
import json


from titbit.models import Comment, UserProfile, Post


class TestAllPosts(TestCase):
    def setUp(self) -> None:
        return super().setUp()
        self.client = Client()

    def test_all_posts_list_view(self):
        message = "TESTE"
        marlos = User(username="marlos")
        marlos.save()
        post = Post(author=marlos, content=message)
        post.save()
        self.assertTrue(post.content.__contains__("TESTE"))
        response = self.client.get(reverse('post-list'))
        self.assertEquals(response.status_code, 302)
