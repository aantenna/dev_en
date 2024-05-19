from django.shortcuts import render
from django.http import HttpResponse

from tracks.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': "Создай свой первый плейлист и начни слушать музыку!",
        'categories': categories

    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "Что мы можем предложить?",
        'text_on_page': 'Добро пожаловать на наш музыкальный сервис, MIS!'

    }
    return render(request, 'main/about.html', context)

