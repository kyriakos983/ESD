from datetime import datetime

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

def dob_validation(value):
    if value > datetime.date.today():
        raise forms.ValidationError('Error enter date before current year')
    return value
class AddClubRepForm(ModelForm):
    date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}))
    dob = forms.DateField(validators=[dob_validation])

    class Meta:
        model = ClubRep
        fields = '__all__'
        labels = {
            'dob': 'Date of Birth',
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ('accountOptions', )

class ScreenShowingForm(ModelForm):
    time = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}))
    class Meta:
        model = ScreenShowing
        fields = '__all__'
