from django.contrib.auth.models import User, Group
from theater.models import *
from django.urls import reverse
from django.test import TestCase, Client
import json
from django.urls import reverse
from customer.views import index

class TestViews_customer(TestCase):

	def setUp(self):
		self.user = User.objects.create_user(username="example",password="Newpassword123",email="example@gmail.com")
		self.profile = Profile.objects.create(user=self.user,theater_name="sawad",address="sawad",owner_name="sawad",phone_number="1234567890",location="palliyath")
		self.screen = Screen.objects.create(screen_name="sawad",theater=self.user,seating_capacity="100",entry_fee="100",seat_rows="10")
		self.movie=Movie.objects.create(theater=self.user,movie_name="sawad",summery="sawad",start_date="2022-12-2",end_date="2022-12-2")
		self.show=Show.objects.create(screen=self.screen,theater=self.user,movie=self.movie,date="2022-12-2",play_time="11:30",status="pending")
		self.load_data_url = reverse('load_data')
		self.booking_url = reverse('booking')

	def test_index_GET(self):
		response = self.client.get(reverse('index'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'customers/index.html')

	def test_movie_details(self):
		response = self.client.get(reverse('movie_details',args=["1"]))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'customers/movie_details.html')

	def test_ticket_plan(self):
		response = self.client.get(reverse('ticket_plan',args=["1"]))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'customers/ticket_plan.html')

	def test_load_data(self):
		data = {'pk': 1,
                'location': 'palliyath',
                'date': '2022-12-2'
                }

		response = self.client.post(self.load_data_url,data)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'customers/load_data.html')

	def test_seat_plan(self):
		response = self.client.get(reverse('seat_plan',args=["1"]))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'customers/seat_plan.html')

	def test_booking(self):
		self.client.login(username='example', password="Newpassword123")
		data = {'seats': 1,
                'show_id': 1,
                'price': 100
                }

		response = self.client.post(self.booking_url,data)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'customers/booking_summery.html')

	def test_my_bookings(self):
		self.client.login(username='example', password="Newpassword123")
		response = self.client.get(reverse('my_bookings'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'customers/my_bookings.html')