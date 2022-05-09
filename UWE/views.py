from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, ListView
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django import forms
from django.contrib.auth import get_user_model
from UWE.forms import *
from UWE.models import *

from django.db.models import F


def Home(request):
    context = {}
    return render(request, 'home.html', context)


def about_us(request):
    context = {}
    return render(request, 'about_us.html', context)

def checkout(request):
    user = request.user
    movie = Movies.objects.all()
    bookings = Booking.objects.latest('user_id')
    context = {'movie': movie ,'bookings': bookings, 'user': user }
    # after checkout complete the ticket will be able to be downloaded
    return render(request, 'checkout.html', context)
# view the student view
def MoviesView(request):
    movies = Movies.objects.all()
    screen = Screen.objects.all()
    context = {'movies': movies, 'screen':screen}
    return render(request, 'films.html', context)

def BookingsView(request):
    movies = Movies.objects.all()
    screen = Screen.objects.all()
    bookings = Booking.objects.all()
    context = {'movies': movies, 'screen':screen, 'bookings':bookings}
    return render(request, 'bookings.html', context)

# this is the buy tickets view for students
def BuyTicketsView(request, id):
    user = request.user
    movie = get_object_or_404(Movies, pk=id)
    screen = Screen.objects.filter(movie = id )
    bookings = Booking.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('checkout')
    else:
        form = BookingForm()
    context = {'screen': screen ,'movie': movie,'form': form, 'bookings': bookings, 'user': user}
    return render(request, 'buyTickets.html', context)


# this is for cinema manager
def addMovie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovieForm()
    return render(request, 'addFilm.html', {'form': form})

#Set screen showing for movies (CINEMA MANAGER)
def addScreenShowing(request):
    if request.method == 'POST':
        form = ScreenShowingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('films')
    else:
        form = ScreenShowingForm()
    return render(request, 'addShowing.html', {'form': form})

# update a current showing of the film
class updateShowings(UpdateView):
    model = Screen
    fields = '__all__'
    template_name = 'updateShowing.html'
    success_url = reverse_lazy('home')

    @staticmethod
    def get_absolute_url():
        return reverse('home')



# this is for cinema manager to be  able to delete a stored movie
def delete_movie(request, id):
    movie = get_object_or_404(Movies, pk=id)
    # posting and storing the data in the database
    if request.method == 'POST':
        movie.delete()
        return redirect('films')

    return render(request, "delete.html", {'movie': movie})


# a cinema manager will be able to register a club
def addClub(request):
    if request.method == 'POST':
        form = AddClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddClubForm()
    return render(request, 'addClub.html', {'form': form})


#  cinema manager will be able to add club representative
def addClubRep(request):
    if request.method == 'POST':
        form = AddClubRepForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddClubRepForm()
    return render(request, 'addClubRep.html', {'form': form})


# cinema manager will be able to update movie details of a selected film
class updateMovieView(UpdateView):
    model = Movies
    fields = '__all__'
    template_name = 'updateMovie.html'
    success_url = reverse_lazy('home')

    @staticmethod
    def get_absolute_url():
        return reverse('home')


# student will be able to access the movie details
def movie_details(request, name, id):
    movie = Movies.objects.get(id=id)
    screen = Screen.objects.all()
    context = {'movie': movie, 'screen':screen}
    return render(request, 'movieDetails.html', context)

def user_Selection(request):
    User = get_user_model()
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'UserSelection.html',context )


class accountAmmend(UpdateView):
    model = User
    fields = '__all__'
    template_name = 'accountAmend.html'
    success_url = reverse_lazy('home')

    @staticmethod
    def get_absolute_url():
        return reverse('home')