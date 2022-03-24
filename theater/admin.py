from django.contrib import admin
from .models import *
from accounts.models import *
from .tasks import send_mail_func,test_func

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('owner_name', 'theater_name', 'address' , 'phone_number','photo','location')
	ordering = ('theater_name',)
	search_fields = ('theater_name', 'location')
	#test_func.delay()

class ScreenAdmin(admin.ModelAdmin):
	list_display = ('theater', 'screen_name', 'seating_capacity', 'entry_fee')
	ordering = ('theater','screen_name')
	search_fields = ('screen_name',)

class MovieAdmin(admin.ModelAdmin):
	list_display = ('movie_name', 'theater', 'start_date', 'end_date',)
	ordering = ('movie_name','theater')
	search_fields = ('movie_name',)

class ShowAdmin(admin.ModelAdmin):
	list_display = ('movie', 'screen', 'theater', 'date', 'play_time','status')
	ordering = ('movie','screen', 'date', 'play_time')
	search_fields = ('date',)

admin.site.register(Profile,)#ProfileAdmin)
admin.site.register(Screen, ScreenAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Show, ShowAdmin)
