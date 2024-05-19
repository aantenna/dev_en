
from django.urls import path
from tracks import views

app_name = 'tracks'

urlpatterns = [
    path('', views.сategories, name='index'),
    path('track/', views.track, name='track'),
]