from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Song
from django.views.generic.edit import CreateView

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def songs_index(request):
    songs = Song.objects.all()
    return render(request, 'songs/index.html', { 'songs': songs})

class SongCreate(CreateView):
    model = Song
    fields = '__all__'

def songs_details(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'songs/details.html', {'song' : song})