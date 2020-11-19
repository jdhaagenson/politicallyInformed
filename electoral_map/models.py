from django.db import models

from voters.models import Voter

# class ElectoralMap(models.Model):
class State(models.model):
    name = models.CharField(max_length=20)
    abbrv = models.CharField(max_length=2)
    electoral = models.IntegerField()
    VAP = models.IntegerField()
    actual_votes = models.IntegerField()
    registered_voters = models.ForeignKey(Voter, on_delete=models.CASCADE)