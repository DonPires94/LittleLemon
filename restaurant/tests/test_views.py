from django.test import TestCase
from django.contrib.auth.models import User

from restaurant.views import MenuItemView
from restaurant.models import MenuItem


class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Pasta", price=15.75, inventory=10)
        MenuItem.objects.create(title="Gelato", price=5.95, inventory=50)
        MenuItem.objects.create(title="Pizza", price=11.25, inventory=25)
        user = User(username="littlelemon", email="testing@littlelemon.com")
        user.set_password("lemon@123!")
        user.save()

    def test_getall(self):
        self.client.login(username="littlelemon", password="lemon@123!")
        response = self.client.get("/menu/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
