from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid




class Accounts(models.TextChoices):
    is_student = 'is_student'
    is_clubRep = 'is_clubRep'
    is_cinema_manager = 'is_cinema_manager'
    is_accounts_manager = 'is_accounts_manager'



# Abstract user class with options for different user accounts.
class User(AbstractUser):
    accountOptions = models.CharField(max_length=50, choices=Accounts.choices, default=None, null=True, blank=True)
    #tickets = models.ForeignKey(ticket,on_delete=models.CASCADE)
    # bookings = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)

class MyUUIDModel(models.Model):
    uniqueId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


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
    dob = models.DateField(default=datetime.strptime('2020-12-31', '%Y-%m-%d'))
    # club_rep_number = models.CharField(max_length=1300,null=True,blank=True,unique=True, default=uuid.uuid4())
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
    image = models.ImageField(upload_to='images/', null=True, blank=True)
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

class Screen(models.Model):
    # check how you can
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE, null=True, blank=True)
    screen = models.CharField(max_length=50, choices=screenChoices.choices, null=True, blank=True)
    tickets = models.IntegerField(default=300, max_length=300)
    ticketPrice = models.IntegerField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.time)


class Booking(models.Model):
    #booking_uniqueID = models.CharField(max_length=100,null=True,blank=True,unique=True, default=uuid.uuid4())
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, null=True, blank=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_Number = models.BigIntegerField()
    Age = models.IntegerField()
    Seats_quantity = models.IntegerField(max_length = 100, null=True, blank=True)
    Showing = models.ForeignKey(Screen,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.Showing.time)

    @property
    def get_total(self):
        total = self.Showing.ticketPrice * self.Seats_quantity
        return total








