from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.test import TestCase, Client
import json
from django.urls import reverse
from customer.views import index
class TestViews_accounts(TestCase):

	def setUp(self):
		self.client = Client()
		self.signup_form_url = reverse('signup_form')
		self.signin_form_url = reverse('signin_form')
		self.signup_url = reverse('signup')
		self.signin_url = reverse('signin')
		self.signout_url = reverse('signout')
		#self.myaccount_url = reverse('myaccount')
		self.delete_url = reverse('delete')
		self.user = User.objects.create_user(username="example",password="Newpassword123")

	def test_project_signup_form_GET(self):
		response = self.client.get(self.signup_form_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'accounts/signup_form.html')

	def test_project_signin_form_GET(self):
		response = self.client.get(self.signin_form_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'accounts/signin_form.html')

	def test_signup(self):
		data = {"email": 'example1@gmail.com',
				"username": 'example1',
                "password": 'Newpassword123'
                }
		response = self.client.post(self.signup_url,data)
		self.assertRedirects(response, reverse(index), status_code=302, 
		target_status_code=200, fetch_redirect_response=True)


	def test_signin(self):
		data = {"username": 'example',
                "password": 'Newpassword123'
                }


		response = self.client.post(self.signin_url,data)
		self.assertRedirects(response, reverse(index), status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

	def test_signin_userNone(self):
		data = {"username": 'None',
                "password": 'Newpassword123'
                }


		response = self.client.post(self.signin_url,data)
		self.assertRedirects(response, reverse('signin_form'), status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
	
	def test_signout(self):

		self.client.login(username='example', password="Newpassword123")

		response = self.client.post(self.signout_url)
		self.assertRedirects(response, reverse('signin_form'), status_code=302, 
		target_status_code=200, fetch_redirect_response=True)

	def test_delete_user(self):

		self.client.login(username='example', password="Newpassword123")

		response = self.client.post(self.delete_url)
		self.assertRedirects(response, reverse(index), status_code=302, 
		target_status_code=200, fetch_redirect_response=True)

