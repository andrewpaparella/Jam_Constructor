from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Song

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def songs_index(request):
    songs = Song.objects.all()
    return render(request, 'songs/index.html', { 'songs': songs})