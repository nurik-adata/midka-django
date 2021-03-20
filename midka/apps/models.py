from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.managers import CustomUserManager
from enum import Enum

class TypeChoice(Enum):
    BU = "Bulet"
    FO = "Food"
    TR = "Travel"
    SP = "Sport"

class User(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class BookJournalBase(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateField()

    class Meta :
        abstract = True


    def __str__(self):
        return self.name

class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=255)

class Journal(BookJournalBase):
    type = models.CharField(
        max_length=255,
        choices=[(tag, tag.value) for tag in TypeChoice]
    )
    publisher = models.CharField(max_length=255)
