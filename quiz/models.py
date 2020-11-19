from django.db import models


class Stance(models.Model):
    topic = models.CharField(max_length=100)
    stance = models.CharField(max_length=250)

    def __str__(self):
        return self.topic

class Quiz(models.Model):
    answers = models.ForeignKey(Stance, on_delete=models.CASCADE)
    questions = models.CharField(max_length=120)