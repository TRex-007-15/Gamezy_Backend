from django.urls import path
from .views import PlayerProfileView

urlpatterns = [
    path('<int:player_id>/', PlayerProfileView.as_view(), name='player_profile_view'),
]
