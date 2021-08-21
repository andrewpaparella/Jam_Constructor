from django.db.models import fields
from django.forms import ModelForm
from .models import Playlist, ReviewPlaylist, ReviewSong

class AddSongForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ['song']

class AddReviewPlaylistForm(ModelForm):
    class Meta:
        model = ReviewPlaylist
        fields = ['content', 'rating']

class AddReviewSongForm(ModelForm):
    class Meta:
        model = ReviewSong
        fields = ['content', 'rating']