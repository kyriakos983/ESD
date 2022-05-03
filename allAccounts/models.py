from django.db import models
from django.contrib.auth.models import AbstractUser

# Account options
class Accounts(models.TextChoices):
    is_student = 'is_student'
    is_clubRep = 'is_clubRep'
    is_cinema_manager = 'is_cinema_manager'
    is_accounts_manager = 'is_accounts_manager'


# Extend the  different user is it
class User(AbstractUser):
    accountOptions = models.CharField(max_length=50, choices=Accounts.choices, default=None, null=True, blank=True)

