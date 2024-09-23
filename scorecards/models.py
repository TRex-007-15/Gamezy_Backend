from django.db import models
from matches.models import Match

class Scorecard(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    team_a_score = models.IntegerField()
    team_b_score = models.IntegerField()
    # Add more fields for player performances if needed
