from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from playlists.models import Playlist
# from playlists.utils import get_user_carts

from tracks.models import Tracks

def playlist_add(request, track_slug):
    # track_id = request.POST.get("track_id")

    track = Tracks.objects.get(slug=track_slug)

    if request.user.is_authenticated:
        playlists = Playlist.objects.filter(user=request.user, track=track)

        if playlists.exists():
            playlist = playlists.first()
            if playlist:
                playlist.save()
        else:
            Playlist.objects.create(user=request.user, track=track)

    return redirect(request.META['HTTP_REFERER'])

def playlist_change(request, track_slug):
    ...


def playlist_remove(request, track_slug):
    ...