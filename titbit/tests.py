from django.test import TestCase
from django.test import Client
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.contrib.auth.models import User
from http import HTTPStatus
from titbit.models import Post


class TestPosts(TestCase):
    def setUp(self) -> None:
        return super().setUp()
        self.client = Client()

    def test_all_posts_list_view_post(self):
        message = "TESTE"
        user_test = User(username="user_test")
        user_test.save()
        post = Post(author=user_test, content=message)
        post.save()
        self.client.force_login(user_test)
        response = self.client.post(reverse('post-list'),
                                    {"content": message, "author": user_test})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(post.content.__contains__("TESTE"))

    def test_delete_post(self):
        message = "TESTE"
        user_test = User(username="user_test")
        user_test.save()
        post = Post(author=user_test, content=message)
        post.save()
        self.client.force_login(user_test)
        response = self.client.delete(reverse("post-delete",
                                      kwargs={"pk": post.id}))
        self.assertEqual(response.status_code, 302)
        # redirect to "home"
        self.assertRedirects(response, "/titbit/", status_code=302)
