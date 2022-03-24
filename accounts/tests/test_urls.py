from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import signup_form, signin_form, signup, signin, signout, myaccount, delete

class TestUrls_accounts(SimpleTestCase):

	def test_signin_form_urls_is_resolves(self):
		url = reverse('signup_form')
		self.assertEquals(resolve(url).func, signup_form)

	def test_signup_form_urls_is_resolves(self):
		url = reverse('signin_form')
		self.assertEquals(resolve(url).func, signin_form)

	def test_signup_urls_is_resolves(self):
		url = reverse('signup')
		self.assertEquals(resolve(url).func, signup)

	def test_signin_urls_is_resolves(self):
		url = reverse('signin')
		self.assertEquals(resolve(url).func, signin)

	def test_myaccount_urls_is_resolves(self):
		url = reverse('myaccount')
		self.assertEquals(resolve(url).func, myaccount)

	def test_delete_urls_is_resolves(self):
		url = reverse('delete')
		self.assertEquals(resolve(url).func, delete)

	#cbv .fun.view_class
	#arg_url ,['args=["1"]] 