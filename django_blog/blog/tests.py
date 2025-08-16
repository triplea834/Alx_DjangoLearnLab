from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Tag  # Tag only if manual

User = get_user_model()

class TagSearchTests(TestCase):
    def setUp(self):
        u = User.objects.create_user('u','u@test.com','pass')
        p1 = Post.objects.create(title='Hello world', content='foo', author=u)
        p2 = Post.objects.create(title='Search me', content='bar', author=u)
        # with taggit:
        p1.tags.add('python','tutorial')
        p2.tags.add('django','python')

    def test_search_by_keyword(self):
        r = self.client.get('/search/?q=Hello')
        self.assertContains(r, 'Hello world')

    def test_search_by_tag(self):
        r = self.client.get('/tags/python/')
        self.assertContains(r, 'Hello world')
        self.assertContains(r, 'Search me')