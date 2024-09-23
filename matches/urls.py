from django.urls import path
from .views import MatchPredictionView, MatchCreateView

urlpatterns = [
    path('predict/<int:match_id>/', MatchPredictionView.as_view(), name='match_prediction'),
    path('create/', MatchCreateView.as_view(), name='create_match'),
]
