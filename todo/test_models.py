from django.test import TestCase

# Create your tests here.

class TestDjango(TestCase):


    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(item, done)


    def test_item_string_method_returns_name():
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')