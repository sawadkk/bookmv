#python
from datetime import date

#django
from django.conf import settings
from django.http.response import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
#thirdpary
import razorpay

#local
from .models import *
from theater.models import *
from theater.tasks import test_func
global today 
today = date.today()

razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def index(request):
	show = Show.objects.select_related("movie")
	test_func.delay()
	if cache.get(show):
		print("hello")
	else:
		print("main")
	return render(request,'customers/index.html',{'show':show})

def movie_details(request, movie_pk):
	movie = Movie.objects.filter(id=movie_pk)
	return render(request,'customers/movie_details.html',{'movie':movie})

def ticket_plan(request, movie_pk):
	movie = Movie.objects.filter(id=movie_pk)
	show = Show.objects.filter(date=today,movie__in=movie)
	show2 = Show.objects.filter(movie__in=movie)
	dates = []
	if cache.get(movie_pk):
		dates = cache.get(movie_pk)
		print("hits the redis")
	else:
		try:
			for i in show2:
				date = str(i.date)
				dates.append(date)
				print("hits db")
				cache.set(movie_pk,dates)
		except:
			return HttpResponse("oops")	
	
	return render(request,'customers/ticket_plan.html',{'shows':show,'movie':movie,'dates':dates})
def load_data(request):
	if request.method == 'POST':
		location = request.POST['location']
		date2 = request.POST['date']
		print(date2)
		movie_pk = request.POST['pk']
		#print(movie_pk)
		movie = Movie.objects.filter(id=movie_pk)
		#show = Show.objects.filter(date=date2,movie__in=movie)
		show2 = Show.objects.filter(movie__in=movie)
		dates = []
		if cache.get(movie_pk):
			dates = cache.get(movie_pk)
			print("hits the redis")
		else:
			try:
				for i in show2:
					date = str(i.date)
					dates.append(date)
					print("hits db")
				cache.set(movie_pk,dates)
			except:
				return HttpResponse("oops")
		
		show = Show.objects.filter(date=date2,movie__in=movie)

		return render(request,'customers/load_data.html',{'shows':show,'movie':movie,'dates':dates})
	return redirect(index)

def seat_plan(request, show_pk):
	show = Show.objects.filter(id=show_pk)
	booking = Booking.objects.filter(show=show_pk)

	book_lst = []
	for book in booking:
		book_lst.append(int(book.seat_number))

	max_seat = 0
	for seat in show:
		max_seat = (seat.screen.seating_capacity)

	seat_lst = []

	for seat in range(1,max_seat+1):
		seat_lst.append(seat)

	return render(request,'customers/seat_plan.html',{'shows':show,'seat':seat_lst,'book':book_lst,'max_seat':max_seat})

@login_required(login_url='signin_form')
def booking(request):
	razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
	if request.method == 'POST':
		seats = request.POST['seats']
		show_id = request.POST['show_id']
		price = request.POST['price']
		show = Show.objects.get(id=show_id)
		seat = seats.split(",")
		length = len(seat)

		#razopay
		currency = 'INR'
		amount = (length*int(price))
		razorpay_order = razorpay_client.order.create(dict(amount=amount*100,currency=currency,payment_capture='0'))
		razorpay_order_id = razorpay_order['id']
		callback_url = 'paymenthandler/'
		context = {}
		context['razorpay_order_id'] = razorpay_order_id
		context['razorpay_merchent_key'] = settings.RAZOR_KEY_ID
		context['razorpay_amount'] = amount
		context['currency'] = currency
		context['callback_url'] = callback_url

		for seat_index in range(length):
			seat_number = seat[seat_index]
			pending  = Booking.objects.create(user=request.user,show=show,seat_number=seat_number,status='Pending')

		#sawad = str(request.user.username)
		#user = User.objects.get(username=sawad)
		#theater_username = show.theater.username
		#theater = User.objects.get(username=theater_username)
		#theater_username1 = str(theater)
		#task_notify.delay(user=sawad,theater=theater_username1,show_id=show_id)
		return render(request,'customers/booking_summery.html',context=context) 
	return redirect('index')

@csrf_exempt
def paymenthandler(request):
	if request.method == 'POST':
		try:
			payment_id = request.POST.get('razorpay_payment_id','')
			razorpay_order_id = request.POST.get('razorpay_order_id','')
			signature = request.POST.get('razorpay_signature','')
			params_dict = {
			'razorpay_order_id':razorpay_order_id,
			'razorpay_payment_id':payment_id,
			'razorpay_signature':signature
			}


			result = razorpay_client.utility.verify_payment_signature(params_dict)
			if result is None:
				print(params_dict)
				amount = 12000
				print('SAWAD')
				try:
					razorpay_client.payment.capture(payment_id,amount)
					return render(request,'payment/paymentsuccess.html')
				except:
					return render(request,'payment/paymentfail.html')
			else:
				return render(request,'payment/paymentfail.html')
		except:
			return HttpResponseBadRequest()
	else:
		return HttpResponseBadRequest()

def my_bookings(request):
	booking = Booking.objects.filter(user=request.user)
	today = str(date.today())
	return render(request,'customers/my_bookings.html',{'booking':booking,'today':today})