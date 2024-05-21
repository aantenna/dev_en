
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('users-playlist/', views.users_playlist, name='users_playlist'),
    path('logout/', views.logout, name='logout'),
]