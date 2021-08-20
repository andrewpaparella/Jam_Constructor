from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Playlist, Song


# Create your views here.
# class PlaylistCreate(CreateView):
#     model = Playlist
#     fields = ["title", "song"]


# class PlaylistUpdate(UpdateView):
#     model = Playlist
#     fields = ["title", "song"]


# class PlaylistDelete(DeleteView):
#     model = Playlist
#     success_url = "/playlists/"


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def songs_index(request):
    songs = Song.objects.all()
    return render(request, "songs/index.html", {"songs": songs})


def songs_details(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, "songs/details.html", {"song": song})


def playlists_index(request):
    playlists = Playlist.objects.all()
    return render(request, "playlists/index.html", {"playlists": playlists})


def playlists_details(request, playlist_id):
    playlists = Playlist.objects.get(id=playlist_id)
    return render(request, "playlists/details.html", {"playlists": playlists})


class SongCreate(CreateView):
    model = Song
    fields = "__all__"
