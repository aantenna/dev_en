
from django.urls import path
from tracks import views

app_name = 'tracks'

urlpatterns = [
    path('', views.сategories, name='index'),
    path('track/<slug:track_slug>/', views.track, name='track'),

]