from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customer.views import index
from .forms import *
from django.db import transaction
from accounts.models import *
from customer.models import *
from django.db import models
#from .tasks import send_mail_func,test_func
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from django.contrib.auth import get_user_model
#from sesame.utils import get_token
#from sesame.utils import get_query_string
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.db.models import Count

def test(request):
    return HttpResponse("Done")

def test2(request, token_user):
#    backend = 'sesame.backends.ModelBackend'
#    User = authenticate(sesame=token_user)
#    login(request,User,backend='sesame.backends.ModelBackend')
    return redirect(index)

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")

@login_required(login_url='signin_form')
def dashboard(request):
    user=request.user
    if user.groups.filter(name='theater').exists():
        screen = Screen.objects.filter(theater=request.user).annotate(shows=Count('show'))

        return render(request,'theater/dashboard.html',{'room_name':'push','screen':screen})
    else:
        messages.info(request,"permission denied")
        return redirect('index')

@login_required(login_url='signin_form')
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,('Your profile was successfully updated!'))
            return redirect('dashboard')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'theater/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def add_screen(request):
    form = ScreenForm()
    if request.method == 'POST':
        print(1)
        form = ScreenForm(request.POST)
        if form.is_valid():
            screen = Screen()
            screen.screen_name = form.cleaned_data['screen_name']
            screen.theater = request.user
            screen.seating_capacity = form.cleaned_data['seating_capacity']
            screen.entry_fee = form.cleaned_data['entry_fee']
            screen.seat_rows = form.cleaned_data['seat_rows']
            screen.save()
            if request.user.is_active:
                print('active')
            else:
                 instance.is_active = True
                 print('is active now')
            messages.success(request,('screen added'))
            return redirect('dashboard')
        else:
            messages.error(request, ('Please correct the error below.'))
            return render(request,'theater/add_screen.html',{'screen_form':form})
    return render(request,'theater/add_screen.html',{'screen_form':form})

def update_screen(request, screen_pk):
    item = Screen.objects.get(pk=screen_pk)
    updateForm = ScreenForm(instance=item)
    if request.method=='POST':
        screenAdd = ScreenForm(request.POST,instance=item)
        if screenAdd.is_valid():
            screenAdd.save()
            messages.success(request, 'Screen has been updated.')
            return redirect('dashboard')
        else:
            messages.success(request, 'oops validation failed')
            return render(request,'theater/update_screen.html',{
                'form':updateForm,
                'item':item
                })
    data = Screen.objects.filter(pk=screen_pk)
    return render(request,'theater/update_screen.html',{
        'form':updateForm,
        'item':data
    })

def screen_delete(request,screen_pk):
    if Screen.objects.filter(id=screen_pk,theater=request.user):
        Screen.objects.get(id=screen_pk).delete()
        messages.success(request,'screen deleted')
        return redirect('dashboard')
    return redirect('index')

def add_movie(request):
    form = MovieForm()
    if request.method == 'POST':
        print(1)
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = Movie()
            movie.theater = request.user
            movie.movie_name = form.cleaned_data['movie_name']
            movie.poster_image = form.cleaned_data['poster_image']
            movie.summery = form.cleaned_data['summery']
            movie.start_date = form.cleaned_data['start_date']
            movie.end_date = form.cleaned_data['end_date']
            movie.trailer_link = form.cleaned_data['trailer_link']
            movie.save()
            messages.success(request,('movie added'))
            return redirect('dashboard')
        else:
            messages.error(request, ('Please correct the error below.'))
            return render(request,'theater/add_movie.html',{'movie_form':form})
    return render(request,'theater/add_movie.html',{'movie_form':form})

def update_movie(request, movie_pk):
    item = Movie.objects.get(pk=movie_pk)
    updateForm = MovieForm(instance=item)
    if request.method=='POST':
        movieAdd = MovieForm(request.POST,instance=item)
        if movieAdd.is_valid():
            movieAdd.save()
            messages.success(request, 'movie has been updated.')
            return redirect('dashboard')
        else:
            messages.success(request, 'oops validation failed')
            return render(request,'theater/update_movie.html',{
                'form':updateForm,
                'item':item
                })
    data = Movie.objects.filter(pk=movie_pk)
    return render(request,'theater/update_movie.html',{
        'form':updateForm,
        'item':data
    })

def movie_delete(request,movie_pk):
    if Movie.objects.filter(id=movie_pk,screen=5):
        Movie.objects.get(id=movie_pk).delete()
        messages.success(request,'movie deleted')
        return redirect('dashboard')
    return redirect('index')

from django.db.models import Count
from django.db.models import Q
def screen_shows(request,screen_pk):
    pending = Count('booking', filter=Q(booking__status='Pending'))
    approved = Count('booking', filter=Q(booking__status='Approved'))
    show = Show.objects.filter(screen=screen_pk).annotate(approved_requests=approved,pending_requests=pending).select_related('screen')
    return render(request,'theater/screen_shows.html',{'show':show})

def add_show(request, screen_pk):
    form = ShowForm()
    if request.method == 'POST':
        print(1)
        form = ShowForm(request.POST)
        if form.is_valid():
            show = Show()
            show.screen = Screen.objects.get(pk=screen_pk)
            show.theater = request.user
            show.movie = form.cleaned_data['movie']
            show.date = form.cleaned_data['date']
            show.play_time = form.cleaned_data['play_time']
            show.save()
            messages.success(request,('show added'))
            return redirect('dashboard')
        else:
            messages.error(request, ('Please correct the error below.'))
            return render(request,'theater/add_show.html',{'show_form':form})
    screen = Screen.objects.filter(pk=screen_pk)
    sawad = screen_pk
    return render(request,'theater/add_show.html',{'show_form':form,'screen':screen})

def update_show(request, show_pk):
    item = Show.objects.get(pk=show_pk)
    updateForm = ShowForm(instance=item)
    if request.method=='POST':
        showAdd = ShowForm(request.POST,instance=item)
        if showAdd.is_valid():
            showAdd.save()
            messages.success(request, 'show has been updated.')
            return redirect('dashboard')
        else:
            messages.success(request, 'oops validation failed')
            return render(request,'theater/update_show.html',{
                'form':updateForm,
                'item':item
                })
    data = Show.objects.filter(pk=show_pk)
    return render(request,'theater/update_show.html',{
        'form':updateForm,
        'item':data
    })

def show_delete(request,show_pk):
    if Show.objects.filter(id=show_pk,theater=request.user):
        Show.objects.get(id=show_pk).delete()
        messages.success(request,'show deleted')
        return redirect('dashboard')
    return redirect('index')

def booking_requests(request,show_pk):
    show = Show.objects.filter(id=show_pk)
    booking_requests = Booking.objects.filter(show__in=show,status='Pending')
    return render(request,'theater/booking_requests.html',{'booking_requests':booking_requests,'show':show})

def accept_booking(request, booking_pk):
    if Show.objects.filter(theater=request.user):
        booking = Booking.objects.filter(id=booking_pk)
        booking.update(status="Approved")
        messages.success(request,'booking accepted')
        return redirect(request.META['HTTP_REFERER'])
    messages.error(request,'oops 404')
    return redirect('dashboard')

def reject_booking(request, booking_pk):
    if Show.objects.filter(theater=request.user):
        booking = Booking.objects.filter(id=booking_pk)
        booking.update(status="Rejected")
        messages.success(request,'booking rejected')
        return redirect(request.META['HTTP_REFERER'])
    messages.error(request,'oops 404')
    return redirect('dashboard')