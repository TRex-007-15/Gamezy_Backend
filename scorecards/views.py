from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Scorecard
from .serializers import ScorecardSerializer

class ScorecardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        match_id = kwargs.get('match_id')
        scorecard = Scorecard.objects.get(match__id=match_id)
        serializer = ScorecardSerializer(scorecard)
        return Response(serializer.data)
