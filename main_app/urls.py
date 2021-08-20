from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("songs/", views.songs_index, name="songs_index"),
    path("songs/details/", views.songs_detail, name="songs_details"),
    path("playlists/", views.playlists_index, name="playlists_index"),
    path("playlists/details/", views.playlists_details, name="playlists_details"),
]
