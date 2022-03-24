from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,db_index=True)
    theater_name = models.CharField(max_length = 50)
    address = models.TextField(max_length=500, blank=True) 
    owner_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 50)
    photo = models.ImageField(upload_to = "%y/%m/%d/images",null=True,blank=True)
    location = models.CharField(max_length=30,db_index=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)
			print('created')


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	if Profile.objects.filter(user=instance).exists():
		instance.profile.save()
		print("saved")
		if instance.groups.filter(name='theater').exists():
			print('in theater')
		else:
			Profile.objects.get(user=instance).delete()
			print("no in theater")

class Screen(models.Model):
	screen_name = models.TextField(max_length=50)
	theater = models.ForeignKey(User, on_delete=models.CASCADE,db_index=True)
	seating_capacity = models.IntegerField()
	entry_fee = models.IntegerField()
	seat_rows = models.IntegerField()

	def location(self):
		return self.theater.profile
	
	def __str__(self):
		return self.screen_name

class Movie(models.Model):
	theater = models.ForeignKey(User, on_delete=models.CASCADE,db_index=True)
	movie_name = models.TextField(db_index=True)
	poster_image = models.ImageField(upload_to='thumbnails/')
	trailer_link = models.URLField(blank=True,null=True)
	summery = models.TextField()
	start_date = models.DateField()
	end_date = models.DateField()

	def __str__(self):
		return self.movie_name

class Show(models.Model):
	CHOICES_PLAY = (
        ('8:30-AM', '8:30'),
        ('11:30-AM', '11:30'),
        ('2:30-PM', '14:30'),
        ('5:30-PM', '17:30'),
        ('8:30-PM', '20:30'),
    )
	CHOICES_STATUS = (
        ('Empty', 'empty'),
        ('Filling', 'filling'),
        ('Housefull', 'housefull'),
        ('Cancelled', 'cancelled'),
    )
	screen = models.ForeignKey(Screen, on_delete=models.CASCADE,db_index=True)
	theater = models.ForeignKey(User, on_delete=models.CASCADE,db_index=True)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE,db_index=True)
	date = models.CharField(max_length=300,db_index=True)
	play_time = models.CharField(max_length=300, choices=CHOICES_PLAY)
	status = models.CharField(max_length=300, choices=CHOICES_STATUS,db_index=True)

	def __str__(self):
		return str(self.movie.movie_name)+str(self.date)+str(self.play_time)


