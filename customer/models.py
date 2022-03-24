from django.db import models
from django.contrib.auth.models import User
from theater.models import *

class Booking(models.Model):
	CHOICES_STATUS = (
        ('Pending', 'Pen'),
        ('Approved', 'App'),
        ('Rejected', 'Rej'),
        ('Cancelled-User', 'Can-U'),
        ('Cancelled-Theater', 'Can-T'),
    )

	user = models.ForeignKey(User, on_delete=models.CASCADE,db_index=True)
	show = models.ForeignKey(Show, on_delete=models.CASCADE,db_index=True)
	seat_number = models.CharField(max_length=50)
	status = models.CharField(max_length=300, choices=CHOICES_STATUS)

