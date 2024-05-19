from django.shortcuts import render
from tracks.models import Tracks

def сategories(request):

    tracks = Tracks.objects.all() # помещаем QuerySet - набор из базы данных

    context = {
        'title': 'Home - Категории',
        'tracks': tracks,
    }
    return render(request, 'tracks/categories.html', context)


def track(request, track_slug):

    track = Tracks.objects.get(slug=track_slug)

    context = {
        'track': track
    }

    return render(request, 'tracks/track.html', context=context)
