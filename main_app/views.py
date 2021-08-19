from django.http.response import HttpResponse
from django.shortcuts import render
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
