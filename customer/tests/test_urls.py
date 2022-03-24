from django.test import SimpleTestCase
from django.urls import reverse, resolve
from customer.views import *

class TestUrls_customer(SimpleTestCase):

	def test_index_urls_is_resolves(self):
		url = reverse('index')
		self.assertEquals(resolve(url).func, index)

	def test_movie_details_urls_is_resolves(self):
		url = reverse('movie_details',args=["1"])
		self.assertEquals(resolve(url).func, movie_details)

	def test_ticket_plan_urls_is_resolves(self):
		url = reverse('ticket_plan',args=["1"])
		self.assertEquals(resolve(url).func, ticket_plan)

	def test_load_data_urls_is_resolves(self):
		url = reverse('load_data')
		self.assertEquals(resolve(url).func, load_data)

	def test_seat_plan_urls_is_resolves(self):
		url = reverse('seat_plan',args=["1"])
		self.assertEquals(resolve(url).func, seat_plan)

	def test_booking_urls_is_resolves(self):
		url = reverse('booking')
		self.assertEquals(resolve(url).func, booking)

	def test_paymenthandler_urls_is_resolves(self):
		url = reverse('paymenthandler')
		self.assertEquals(resolve(url).func, paymenthandler)

	def test_my_bookings_urls_is_resolves(self):
		url = reverse('my_bookings')
		self.assertEquals(resolve(url).func, my_bookings)


