from django.test import TestCase
from django.urls import reverse


class BlogViewTest(TestCase):

    def test_blog_home(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')