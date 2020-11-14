from django.contrib.auth.models import AbstractUser
from django.db import models

class Voter(AbstractUser):
    PARTY_CHOICES = (
        ('R', 'Republican'),
        ('D', 'Democrat'),
        ('I', 'Independent'),
        ('G', 'Green Party'),
        ('S', 'Socialist'),
        ('U', 'Unaffiliated')
    )
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
        ('P', 'Private')
    )
    party = models.CharField(max_length=12, choices=PARTY_CHOICES, default='U')
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='P')
    profile_pic = models.URLField(null=True, blank=True)
    REQUIRED_FIELDS = ['email', 'party', 'gender']


