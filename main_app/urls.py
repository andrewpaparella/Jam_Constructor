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
    path("playlists/create/", views.PlaylistCreate.as_view(), name="playlists_create"),
    path(
        "playlists/<int:pk>/update/",
        views.PlaylistUpdate.as_view(),
        name="playlists_update",
    ),
    path("playlists/<int:pk>/delete", views.PlaylistDelete.as_view(), name="playlists_delete"),
    # path('playlists/<int:playlist_id>/add_song/', views.add_song, name='add_song'),
    path("playlists/<int:playlist_id>/assoc_song/<int:song_id>/", views.assoc_song, name="assoc_song"),
    path("playlists/<int:playlist_id>/unassoc_song/<int:song_id>/", views.unassoc_song, name="unassoc_song"),
    path("playlists/<int:playlist_id>/add_playlistreview/", views.add_playlistreview, name="add_playlistreview"),
    path("songs/<int:song_id>/add_songreview/", views.add_songreview, name="add_songreview"),
    path("songs/<int:pk>/update/", views.SongUpdate.as_view(), name="songs_update"),
    path('accounts/signup/', views.signup, name='signup'),
]
