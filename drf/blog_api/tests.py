from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User


class Test_Create_Post(APITestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )
        test_post = Post.objects.create(
            category_id=1, title='Post Title', excerpt='Post Excerpt',
            content='Post Content', slug='post-title', author_id=1,
            status='published'
        )

    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        url = reverse('blog_api:listcreate')
        data = {
            "title": "Post Title",
            "excerpt": "Post Excerpt",
            "content": "Post Content",
            "status": "published",
            "category": 1,
            "author": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)