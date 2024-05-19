from django.shortcuts import render

def сategories(request):
    return render(request, 'tracks/categories.html')

def track(request):
    return render(request, 'tracks/track.html')