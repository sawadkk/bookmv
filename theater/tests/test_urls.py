from django.test import SimpleTestCase
from django.urls import reverse, resolve
from theater.views import *

class TestUrls_accounts(SimpleTestCase):

	def test_dashboard_urls_is_resolves(self):
		url = reverse('dashboard')
		self.assertEquals(resolve(url).func, dashboard)

	def test_update_profile_urls_is_resolves(self):
		url = reverse('update_profile')
		self.assertEquals(resolve(url).func, update_profile)

	def test_add_screen_is_resolves(self):
		url = reverse('add_screen')
		self.assertEquals(resolve(url).func,add_screen)

	def test_update_screen_urls_is_resolves(self):
		url = reverse('update_screen',args=["1"])
		self.assertEquals(resolve(url).func, update_screen)

	def test_screen_delete_urls_is_resolves(self):
		url = reverse('screen_delete',args=["1"])
		self.assertEquals(resolve(url).func, screen_delete)

	def test_add_movie_urls_is_resolves(self):
		url = reverse('add_movie')
		self.assertEquals(resolve(url).func, add_movie)
	
	def test_update_movie_urls_is_resolves(self):
		url = reverse('update_movie',args=["1"])
		self.assertEquals(resolve(url).func, update_movie)
	
	def test_movie_delete_urls_is_resolves(self):
		url = reverse('movie_delete',args=["1"])
		self.assertEquals(resolve(url).func, movie_delete)
	
	def test_add_show_urls_is_resolves(self):
		url = reverse('add_show',args=["1"])
		self.assertEquals(resolve(url).func, add_show)
	
	def test_screen_shows_urls_is_resolves(self):
		url = reverse('screen_shows',args=["1"])
		self.assertEquals(resolve(url).func, screen_shows)
	
	def test_update_show_urls_is_resolves(self):
		url = reverse('update_show',args=["1"])
		self.assertEquals(resolve(url).func, update_show)
	
	def test_show_delete_urls_is_resolves(self):
		url = reverse('show_delete',args=["1"])
		self.assertEquals(resolve(url).func, show_delete)

	def test_booking_requests_urls_is_resolves(self):
		url = reverse('booking_requests',args=["1"])
		self.assertEquals(resolve(url).func, booking_requests)

	def test_accept_booking_urls_is_resolves(self):
		url = reverse('accept_booking',args=["1"])
		self.assertEquals(resolve(url).func, accept_booking)

	def test_reject_booking_urls_is_resolves(self):
		url = reverse('reject_booking',args=["1"])
		self.assertEquals(resolve(url).func, reject_booking)
	

	#cbv .fun.view_class
	#arg_url ,['args=["1"]] 