from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
               path('signupform',views.signup_form,name = 'signup_form'),
               path('signinform',views.signin_form,name = 'signin_form'),
               path('signup',views.signup,name = 'signup'),
               path('signin',views.signin,name = 'signin'),
               path('signout',views.signout,name = 'signout'),
               path('myaccount',views.myaccount,name = 'myaccount'),
               path('delete',views.delete,name = 'delete'),

               ]

