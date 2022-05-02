from django.contrib.admin import widgets
from django.forms import ModelForm
from .models import Movies, ticket, Club, ClubRep
from django.forms.widgets import NumberInput
from django.forms.widgets import TimeInput
from django import forms
from .models import Movies, ticket, Club, ClubRep


class MovieForm(ModelForm):
    date_input2 = forms.TimeField(widget=NumberInput(attrs={'type': 'date'}))
    time_input = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}))

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
    class Meta:
        model = ClubRep
        fields = '__all__'
