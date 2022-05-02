from django.contrib import admin
from UWE.models import Movies, Club, ClubRep

# Register your models here.
from allAccounts.models import User

admin.site.register(Movies)
admin.site.register(User)
admin.site.register(Club)
admin.site.register(ClubRep)