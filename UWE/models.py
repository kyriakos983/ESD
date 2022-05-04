from datetime import datetime

from django.conf import settings
from django.db import models
from allAccounts.models import *


# model for all the  clubs
class Club(models.Model):
    club_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200)
    postCode = models.CharField(max_length=10)
    house_num = models.IntegerField()
    city = models.CharField(max_length=50)
    phone_num = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    clubID = models.IntegerField()

    def __str__(self):
        return self.club_name


# model for all the club representative
class ClubRep(models.Model):
    club = models.OneToOneField(Club, on_delete=models.CASCADE)
    clubRepFirstName = models.CharField(max_length=50)
    clubRepLastName = models.CharField(max_length=50)
    dob = models.DateField(default=datetime.strptime('2022-05-04', '%Y-%m-%d'))
    club_rep_number = models.CharField(max_length=11)
    club_rep_email = models.EmailField(max_length=100, null=True)


# movie types choices
class movieTypes(models.TextChoices):
    Action = 'Action'
    Comedy = 'Comedy'
    Drama = 'Drama'
    Fantasy = 'Fantasy'
    Horror = 'Horror'
    Mystery = 'Mystery'
    Romance = 'Romance'
    Thriller = 'Thriller'


# screen options
class screenChoices(models.TextChoices):
    screen1 = 'screen1'
    screen2 = 'screen2'
    screen3 = 'screen3'
    screen4 = 'screen4'
    screen5 = 'screen5'


# This contains all the details regarding the movies
class Movies(models.Model):
    name = models.CharField(max_length=50)
    ticketPrice = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    # setting the capacity of the screen show by limiting the tickets to 300 mentioned in the requirements

    actor1 = models.CharField(max_length=100, null=True, blank=True)
    actor2 = models.CharField(max_length=100, null=True, blank=True)
    actor3 = models.CharField(max_length=100, null=True, blank=True)
    ageRating = models.IntegerField(null=True, blank=True)
    duration = models.CharField(max_length=15, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    author = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=50, choices=movieTypes.choices, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class ScreenShowing(models.Model):
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE)
    screen = models.CharField(max_length=50, choices=screenChoices.choices, null=True, blank=True)
    tickets = models.IntegerField(default=300, max_length=300)


class TicketDiscount(models.Model):
    total_price = models.IntegerField(default=False)
    sale_price = models.IntegerField(default=False)
    new_price = models.IntegerField(default=False)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ticket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    movie = models.OneToOneField(Movies, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    quantity = models.IntegerField(max_length=300)
    price = models.IntegerField()


# Booking system allows payment type specified to credits, payment authorises when user has paid
class bookingReservation(models.Model):
    payment_type = (
        ('Credits', 'Credits'),
    )
    payment_type = models.CharField(max_length=11, choices=payment_type, default='Credits')
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    paid_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True)


class seatsAvailable(models.Model):
    seat_choice = (
        ('', 'Select'),
        ('Regular', 'Regular'),
        ('V.I.P', 'V.I.P')
    )
    seat_type = models.CharField(max_length=8, choices=seat_choice, blank=False)
    row = models.PositiveSmallIntegerField()
    col = models.PositiveSmallIntegerField()
