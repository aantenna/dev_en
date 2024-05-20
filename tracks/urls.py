
from django.urls import path
from tracks import views

app_name = 'tracks'

urlpatterns = [
    path('search/', views.сategories, name='search'), # URL для поиска
    path('<slug:category_slug>/', views.сategories, name='index'),
    path('track/<slug:track_slug>/', views.track, name='track'),
]