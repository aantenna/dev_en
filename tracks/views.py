from django.shortcuts import render
from tracks.models import Tracks

def сategories(request):

    tracks = Tracks.objects.all() # помещаем QuerySet - набор из базы данных

    context = {
        'title': 'Home - Категории',
        'tracks': tracks,
    }
    return render(request, 'tracks/categories.html', context)


def track(request):
    return render(request, 'tracks/track.html')
