from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Menu, Item, Ingredient
from .forms import MenuForm

menu_data = {
	'season': 'Winter'
}


class MenuViewsTest(TestCase):
	def setUp(self):
		self.testchef = User.objects.create(
			username='user',
			email='test@test.com',
			password='testtesttest'
		)
		ingredient1 = Ingredient(name='ingredient1')
		ingredient1.save()
		ingredient2 = Ingredient(name='ingredient2')
		ingredient2.save()
		self.item1 = Item(
			name='Hamburger',
			description='Comes with cheese',
			chef=self.testchef
		)
		self.item1.save()
		self.item1.ingredients.add(ingredient1, ingredient2)
		self.menu = Menu.objects.create(**menu_data)
		self.menu.items.add(self.item1)
		
	def test_menudetail_view(self):
		resp = self.client.get(reverse('menu_detail',
			kwargs={'pk': self.menu.pk}))
		self.assertEqual(resp.status_code, 200)
		
	def test_menulist_view(self):
		resp = self.client.get(reverse('menu_list'))
		self.assertEqual(resp.status_code, 200)
		
	def test_itemdetail_view(self):
		resp = self.client.get(reverse('item_detail',
			kwargs={'pk': self.item1.pk}))
		self.assertEqual(resp.status_code, 200)