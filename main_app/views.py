from main_app.forms import AddSongForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Playlist, Song


# Create your views here.
class PlaylistCreate(CreateView):
    model = Playlist
    fields = ["title", "song"]


class PlaylistUpdate(UpdateView):
    model = Playlist
    fields = ["title", "song"]


class PlaylistDelete(DeleteView):
    model = Playlist
    success_url = "/playlists/"


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
    playlist = Playlist.objects.get(id=playlist_id)
    add_song_form = AddSongForm()
    return render(request, "playlists/details.html", {"playlist": playlist, 'add_song_form': add_song_form})

def add_song(request, playlist_id):
    form = AddSongForm(request.POST)
    if form.is_valid():
        new_song = form.save(commit=False)
        new_song.playlist_id = playlist_id
        new_song.save()
    return redirect('playlists_details', playlist_id=playlist_id)


class SongCreate(CreateView):
    model = Song
    fields = "__all__"
