from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from blog.models import Category, Post
# Create your tests here.


class BlogModelTest(TestCase):

    def post_create(self):
        author = User.objects.create(username='enas', password='123enas')
        category = Category.objects.create(name='Test_Category', slug='django')

        return Post.objects.create(
            author = author,
            title = 'django_test',
            tags = 'test',
            description = 'django test description',
            category = category,
            slug = 'django'
        )

    def test_model_str(self):
        post = self.post_create()
        self.assertEqual(post.__str__(),post.title)

class CategoryTest(TestCase):

    def category_create(self, name="category test2", slug='django'):
        return Category.objects.create(name=name, slug=slug)

    def test_category_creation(self):
        category = self.category_create()
        self.assertEqual(category.__str__(), category.name)