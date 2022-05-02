from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django import forms

from UWE.forms import *
from UWE.models import *

from django.db.models import F


def Home(request):
    context = {}
    return render(request, 'home.html', context)


def about_us(request):
    context = {}
    return render(request, 'about_us.html', context)


# view the student view
def MoviesView(request):
    movies = Movies.objects.all()
    context = {'movies': movies}
    return render(request, 'films.html', context)


def DiscountView(request):
    discounts = TicketDiscount.objects.annotate(offer=((F('total_price') - F('sale_price')) / F('total_price')) * 100)
    context = {'discounts': discounts}
    return render(request, 'offersAndDiscounts.html', context)


# this is the buy tickets view for students
def BuyTicketsView(request, id):
    movie = get_object_or_404(Movies, pk=id)
    return render(request, 'buyTickets.html', {'movie': movie})

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


# this is for cinema manager
def delete_movie(request, id):
    movie = get_object_or_404(Movies, pk=id)
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


# update details view for cinema manager
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
    return render(request, 'movieDetails.html', {'movie': movie})
