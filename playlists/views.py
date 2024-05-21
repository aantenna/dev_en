from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from playlists.models import Playlist
# from playlists.utils import get_user_carts

from tracks.models import Tracks

def playlist_add(request, track_slug):

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

# def playlist_change(request, track_slug):
#     ...


def playlist_remove(request, playlist_id):
    # cart_id = request.POST.get("cart_id")
    #
    playlist = Playlist.objects.get(id=playlist_id)
    # quantity = cart.quantity
    playlist.delete()
    #
    # user_cart = get_user_carts(request)
    # cart_items_html = render_to_string(
    #     "carts/includes/included_cart.html", {"carts": user_cart}, request=request)
    #
    # response_data = {
    #     "message": "Товар удален",
    #     "cart_items_html": cart_items_html,
    #     "quantity_deleted": quantity,
    # }
    return redirect(request.META['HTTP_REFERER'])
    # return JsonResponse(response_data)
