from django.contrib.auth import get_user_model
from accounts.models import *
from customer.models import *
from theater.models import *
from celery import shared_task
from django.core.mail import send_mail
from book_my_movie import settings
#from notifications.signals import notify

#@shared_task(bind=True)
#def task_notify(self,theater, user, show_id):
   #theater_1 = get_user_model().objects.get(username=theater)
   #user_1 = get_user_model().objects.get(username=user)
   #show = Show.objects.get(pk=show_id)
   #notify.send(theater_1, recipient=user_1, verb='pending booking request created at'+theater_1.loaction)
   #notify.send(user_1, recipient=theater_1, verb='booking request for'+show.movie.movie_name)
#   return 'done'
    

