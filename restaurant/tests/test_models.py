from django.test import TestCase

from restaurant.models import Booking, MenuItem


class MenuItemTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Ice Cream", price=80, inventory=100)

    def test_get_menu_item(self):
        item = MenuItem.objects.get(title="Ice Cream")
        self.assertEqual(item.__str__(), "Ice Cream : 80.00")
