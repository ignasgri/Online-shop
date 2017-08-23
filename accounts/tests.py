from django.test import TestCase

class SimpleTest(TestCase):
    def test_adding_something_simple(self):
        self.assertEqual( 1 + 2, 3 )
