from django.test import TestCase
from ..models import*
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpData")
        pass
    def setUp(self):
        print("setUp:")
        pass
    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)
    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(True)
    def test_number(self):
        print("Method: number")
        post=Posts2()
        self.assertEqual(post.get_number(), 1)
    def test_published (self):
        print("Method: published")
        post=Posts2()
        self.assertTrue(post.is_published)
