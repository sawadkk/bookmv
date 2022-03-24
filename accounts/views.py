from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customer.views import index
from theater.forms import *
from django.db import transaction
from .models import *
from django.db import models
from django.contrib.sessions.models import Session
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse

def signup_form(request):
	print("chabged")
	return render(request,'accounts/signup_form.html')

def signin_form(request):
	return render(request,'accounts/signin_form.html')

def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		
		user = User.objects.create_user(username=username,email=email,password=password)
		#group = Group.objects.get(name="customer")
		#user.groups.add(group)
		print("user created")

		messages.success(request,'user created succesfully')
		login(request,user)
		print("userlogin and registered")
		return redirect(index)
	else:
		return redirect(signup_form)


def signin(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		print(password)
		User = authenticate(username=username,password=password)
		if User is not None:
			login(request,User)
			print("loged")
			user = request.user
			if user.groups.filter(name='theater').exists():
				print("theater-login")
				return redirect('dashboard')
			else:
				print("userlogin")
				return redirect(index)
		else:
			print("no such user")
			messages.info(request,'incorect user name or password')
			return redirect(signin_form)
	else:
		return redirect(signin_form)

@login_required(login_url='signin_form')
def signout(request):
	logout(request)
	print("logout")
	return redirect(signin_form)

def myaccount(request):
	data = User.objects.filter(username=request.user)
	return render(request,'myaccount.html')

@login_required(login_url='signin_form')
def delete(request):
	messages.info(request,"your data will be permenately lost")
	User.objects.get(username=request.user).delete
	messages.success(request,'user deleted')
	return redirect(index)