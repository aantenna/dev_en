
from django.urls import path
from playlists import views

app_name = 'playlists'

urlpatterns = [
    path('playlist_add/<slug:track_slug>/', views.playlist_add, name='playlist_add'),
    path('playlist_change/<slug:track_slug>/', views.playlist_change, name='playlist_change'),
    path('playlist_remove/<slug:track_slug>/', views.playlist_remove, name='playlist_remove'),
]