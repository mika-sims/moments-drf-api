from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='pass')

    def test_can_list_posts(self):
        testuser = User.objects.get(username='testuser')
        Post.objects.create(
            owner=testuser,
            title='test post',
            content='test content',
        )
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_create_post(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.post('/posts/', {
            'title': 'test post',
            'content': 'test content',
        })
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cannot_create_post(self):
        response = self.client.post('/posts/', {
            'title': 'test post',
            'content': 'test content',
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
