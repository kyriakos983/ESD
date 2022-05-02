from django.db import models
from django.contrib.auth.models import AbstractUser


class Accounts(models.TextChoices):
    is_student = 'is_student'
    is_clubRep = 'is_clubRep'
    is_cinema_manager = 'is_cinema_manager'
    is_accounts_manager = 'is_accounts_manager'


# Extend the  different user is it
class User(AbstractUser):
    # Different users of the web application for login identification
    is_student = models.BooleanField('is_student', default=False)
    is_clubRep = models.BooleanField('is_clubRep', default=False)
    is_cinema_manager = models.BooleanField('is_cinema_manager', default=False)
    is_accounts_manager = models.BooleanField('is_accounts_manager', default=False)
    accountOptions = models.CharField(max_length=50, choices=Accounts.choices, default=None, null=True, blank=True)
