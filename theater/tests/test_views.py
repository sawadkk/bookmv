from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.test import TestCase, Client
import json
from django.urls import reverse
from customer.views import index

class TestViews_theater_dashboard(TestCase):
	def setUp(self):
		self.client = Client()
		self.dashboard_url = reverse('dashboard')
		self.user = User.objects.create_user(username="example",password="Newpassword123",email="example@gmail.com")
		Group.objects.create(name="theater")

	def test_dashboard_theater_GET(self):
		self.client.login(username='example', password="Newpassword123")
		my_group = Group.objects.get(name="theater")
		my_group.user_set.add(self.user)

		response = self.client.get(self.dashboard_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'theater/dashboard.html')

	def test_dashboard_customer_GET(self):
		self.client.login(username='example', password="Newpassword123")

		response = self.client.get(self.dashboard_url)
		print("not in theater success")

		self.assertRedirects(response, reverse(index), status_code=302, 
		target_status_code=200, fetch_redirect_response=True) 

#class TestViews_theater_update_profile(TestCase):
