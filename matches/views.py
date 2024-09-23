from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Match
from .serializers import MatchSerializer
import random  # Placeholder for prediction logic

class MatchCreateView(generics.CreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

class MatchPredictionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        match_id = kwargs.get('match_id')
        match = Match.objects.get(id=match_id)
        
        # Placeholder prediction logic: generate random probabilities for teams
        team_a_probability = random.uniform(0, 1)
        team_b_probability = 1 - team_a_probability

        match.team_a_win_probability = round(team_a_probability, 2)
        match.team_b_win_probability = round(team_b_probability, 2)

        if match.team_a_win_probability > match.team_b_win_probability:
            predicted_winner = "team_a"
        else:
            predicted_winner = "team_b"

        match.predicted_outcome = predicted_winner
        match.save()

        return Response({
            'match_id': match.id,
            'team_a': match.team_a,
            'team_b': match.team_b,
            'team_a_win_probability': match.team_a_win_probability,
            'team_b_win_probability': match.team_b_win_probability,
            'predicted_outcome': match.predicted_outcome
        })
