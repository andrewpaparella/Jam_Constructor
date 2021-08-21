from main_app.forms import AddReviewPlaylistForm, AddSongForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Playlist, Song
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class PlaylistCreate(LoginRequiredMixin, CreateView):
    model = Playlist
    fields = ["title"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlaylistUpdate(LoginRequiredMixin, UpdateView):
    model = Playlist
    fields = ["title", "song"]


class PlaylistDelete(LoginRequiredMixin, DeleteView):
    model = Playlist
    success_url = "/playlists/"


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

@login_required
def songs_index(request):
    songs = Song.objects.all()
    return render(request, "songs/index.html", {"songs": songs})

@login_required
def songs_details(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, "songs/details.html", {"song": song})


@login_required
def playlists_index(request):
    playlists = Playlist.objects.all()
    return render(request, "playlists/index.html", {"playlists": playlists})

@login_required
def playlists_details(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    songs_playlist_doesnt_have = Song.objects.exclude(id__in = playlist.song.all().values_list('id'))
    add_song_form = AddSongForm()
    add_reviewplaylist_form = AddReviewPlaylistForm()
    return render(request, "playlists/details.html", {"playlist": playlist, 'add_song_form': add_song_form, 'add_reviewplaylist_form': add_reviewplaylist_form,'songs' : songs_playlist_doesnt_have})

# @login_required
# def add_song(request, playlist_id):
#     form = AddSongForm(request.POST)
#     if form.is_valid():
#         new_song = form.save(commit=False)
#         new_song.playlist_id = playlist_id
#         new_song.save()
#     return redirect('playlists_details', playlist_id=playlist_id)

def add_playlistreview(request, playlist_id):
    form = AddReviewPlaylistForm(request.POST)
    if form.is_valid():
        new_review_playlist = form.save(commit=False)
        new_review_playlist.playlist_id = playlist_id
        new_review_playlist.user_id = request.user.id
        new_review_playlist.save()
    return redirect('playlists_details', playlist_id=playlist_id)

@login_required
def assoc_song(request, playlist_id, song_id):
  Playlist.objects.get(id=playlist_id).song.add(song_id)
  return redirect('playlists_details', playlist_id=playlist_id)

@login_required
def unassoc_song(request, playlist_id, song_id):
  Playlist.objects.get(id=playlist_id).song.remove(song_id)
  return redirect('playlists_details', playlist_id=playlist_id)

class SongCreate(LoginRequiredMixin, CreateView):
    model = Song
    fields = "__all__"

def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('playlists_index')
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context) 