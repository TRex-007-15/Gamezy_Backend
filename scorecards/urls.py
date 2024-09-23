from django.urls import path
from .views import ScorecardView

urlpatterns = [
    path('<int:match_id>/', ScorecardView.as_view(), name='scorecard_view'),
]
