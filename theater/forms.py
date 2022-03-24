from django import forms
from accounts.models import *
from django.contrib.auth.models import User, Group
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('owner_name', 'theater_name', 'address' , 'phone_number','photo','location')
class ScreenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = ('screen_name', 'seating_capacity', 'entry_fee', 'seat_rows')

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('movie_name', 'start_date', 'end_date', 'poster_image', 'trailer_link', 'summery',)

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ('movie', 'date', 'play_time', 'status')
        