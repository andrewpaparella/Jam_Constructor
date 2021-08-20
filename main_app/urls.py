from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("songs/", views.songs_index, name="songs_index"),
    path("songs/create/", views.SongCreate.as_view(), name="songs_create"),
    path("songs/<int:song_id>/", views.songs_details, name="songs_details"),
    path("playlists/", views.playlists_index, name="playlists_index"),
    path(
        "playlists/<int:playlist_id>/",
        views.playlists_details,
        name="playlists_details",
    ),
]
