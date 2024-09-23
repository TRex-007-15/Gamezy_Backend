from django.contrib import admin
from django.urls import path, include  # Import include to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),       # Include user-related URLs
    path('api/matches/', include('matches.urls')),    # Include match-related URLs
    path('api/scorecards/', include('scorecards.urls')),  # Include scorecard-related URLs
    path('api/profiles/', include('profiles.urls')),   # Include profile-related URLs
]
