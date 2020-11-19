from django.contrib.auth.models import AbstractUser
from django.db import models

from quiz.models import Quiz

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
    quiz_answers = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True, default=None)
    image = models.ImageField(upload_to='profile', null=True, blank=True, default='/media/default.png')
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, default=None)
    REQUIRED_FIELDS = ['email', 'party', 'gender']

    def use_default(self):
        self.image = '/static/default.png'

    def __str__(self):
        return self.



