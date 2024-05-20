from django.shortcuts import render, get_list_or_404
from tracks.models import Tracks

def сategories(request, category_slug):

    if category_slug == 'all':
        tracks = Tracks.objects.all()  # помещаем QuerySet - набор из базы данных
    else:
        tracks = get_list_or_404(Tracks.objects.filter(categories__slug=category_slug))



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
