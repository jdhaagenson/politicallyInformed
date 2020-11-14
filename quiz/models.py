from django.db import models


class Stance(models.Model):
    topic = models.CharField(max_length=100)
    stance =