
from django.urls import path
from playlists import views

app_name = 'playlists'

urlpatterns = [
    path('playlist_add/<int:track_id>/', views.playlist_add, name='playlist_add'),
    path('playlist_change/<int:track_id>/', views.playlist_change, name='playlist_change'),
    path('playlist_remove/<int:track_id>/', views.playlist_remove, name='playlist_remove'),
]