from django.contrib.admin import widgets
from django.forms import ModelForm
from .models import Movies, ticket, Club, ClubRep
from django.forms.widgets import DateInput
from allAccounts.models import User
from .models import Movies, ticket, Club, ClubRep, ScreenShowing

from django.forms.widgets import TimeInput
from django import forms
from .models import Movies, ticket, Club, ClubRep


class MovieForm(ModelForm):
    date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Movies
        fields = '__all__'


class ticketForm(ModelForm):
    class Meta:
        model = ticket
        fields = '__all__'
        # exclude = (' ',)


class AddClubForm(ModelForm):
    class Meta:
        model = Club
        fields = '__all__'


class AddClubRepForm(ModelForm):
    date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = ClubRep
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ('accountOptions', )

class ScreenShowingForm(ModelForm):
    class Meta:
        model = ScreenShowing
        fields = '__all__'
