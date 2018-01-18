from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Dad', 'Rolf')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My Dad by Rolf (0 posts)')

    def test_repr_multiple_post(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test post']

        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')

        b2 = Blog('My Dad', 'Rolf')
        b2.posts = ['post1', 'post2']
        self.assertEqual(b2.__repr__(), 'My Dad by Rolf (2 posts)')

