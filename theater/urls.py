from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
               path('dashboard',views.dashboard,name="dashboard"),
               path('update_profile',views.update_profile,name = 'update_profile'),
               path('add_screen',views.add_screen,name = 'add_screen'),
               url(r'^update_screen(?P<screen_pk>\d+)',views.update_screen,name = 'update_screen'),
               url(r'^screen_delete(?P<screen_pk>\d+)/$',views.screen_delete,name='screen_delete'),
               path('add_movie',views.add_movie,name = 'add_movie'),
               url(r'^update_movie(?P<movie_pk>\d+)',views.update_movie,name = 'update_movie'),
               url(r'^movie_delete(?P<movie_pk>\d+)/$',views.movie_delete,name='movie_delete'),
               url(r'^add_show(?P<screen_pk>\d+)',views.add_show,name='add_show'),
               url(r'^screen_shows(?P<screen_pk>\d+)',views.screen_shows,name='screen_shows'),
               url(r'^update_show(?P<show_pk>\d+)',views.update_show,name = 'update_show'),
               url(r'^show_delete(?P<show_pk>\d+)/$',views.show_delete,name='show_delete'),
               url(r'^booking_requests(?P<show_pk>\d+)/$',views.booking_requests,name='booking_requests'),
               path('test',views.test,name = 'test'),
               url(r'^test(?P<token_user>\d+)',views.test2,name='test2'),
               path('send_mail_to_all',views.send_mail_to_all,name = 'send_mail_to_all'),
               url(r'^accept_booking(?P<booking_pk>\d+)',views.accept_booking,name='accept_booking'),
               url(r'^reject_booking(?P<booking_pk>\d+)',views.reject_booking,name='reject_booking'),


               ]

