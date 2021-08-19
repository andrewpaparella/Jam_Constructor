from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('songs/', views.songs_index, name='songs_index'),
    path('songs/create/', views.SongCreate.as_view(), name='songs_create'),
    path('songs/<int:song_id>/', views.songs_details, name="songs_details"),
]
