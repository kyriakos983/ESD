from django.contrib import admin
from UWE.models import Movies, Club, ClubRep, Screen, Booking

# Register your models here.
from allAccounts.models import User

admin.site.register(Movies)
admin.site.register(User)
admin.site.register(Club)
admin.site.register(Screen)
admin.site.register(Booking)
admin.site.register(ClubRep)