from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Player
from .serializers import PlayerSerializer

class PlayerProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        player_id = kwargs.get('player_id')
        player = Player.objects.get(id=player_id)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)
