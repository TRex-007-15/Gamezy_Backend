from django.db import models

class Match(models.Model):
    team_a = models.CharField(max_length=100)
    team_b = models.CharField(max_length=100)
    date = models.DateTimeField()
    predicted_outcome = models.CharField(max_length=10, blank=True)  # Optionally store outcome
    team_a_win_probability = models.FloatField(blank=True, null=True)  # Optionally store probabilities
    team_b_win_probability = models.FloatField(blank=True, null=True)
