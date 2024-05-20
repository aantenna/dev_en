from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from tracks.models import Tracks


def сategories(request, category_slug):

    page = request.GET.get('page', 1)

    if category_slug == 'all':
        tracks = Tracks.objects.all()  # помещаем QuerySet - набор из базы данных
    else:
        tracks = get_list_or_404(Tracks.objects.filter(categories__slug=category_slug))

    paginator = Paginator(tracks, 4)
    current_page = paginator.page(int(page))



    context = {
        'title': 'Home - Категории',
        'tracks': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'tracks/categories.html', context)


def track(request, track_slug):

    track = Tracks.objects.get(slug=track_slug)

    context = {
        'track': track
    }

    return render(request, 'tracks/track.html', context=context)
