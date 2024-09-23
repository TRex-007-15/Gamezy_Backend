from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    profile_image = models.CharField(max_length=100)
    total_runs = models.IntegerField(default=0)
    total_wickets = models.IntegerField(default=0)
