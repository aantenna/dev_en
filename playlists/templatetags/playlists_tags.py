from django import template

from playlists.models import Playlist
# from playlists.utils import get_user_carts


register = template.Library()


@register.simple_tag()
def user_playlists(request):
    if request.user.is_authenticated:
        return Playlist.objects.filter(user=request.user).select_related('track')