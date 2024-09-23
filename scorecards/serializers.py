from rest_framework import serializers
from .models import Scorecard

class ScorecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scorecard
        fields = '__all__'
