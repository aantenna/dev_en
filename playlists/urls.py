
from django.urls import path
from playlists import views
# from .views import playlist_add

app_name = 'playlists'

urlpatterns = [
    path('playlist_add/<slug:track_slug>/', views.playlist_add, name='playlist_add'),
    # path('playlist_change/<slug:track_slug>/', views.playlist_change, name='playlist_change'),
    path('playlist_remove/<int:playlist_id>/', views.playlist_remove, name='playlist_remove'),
]
