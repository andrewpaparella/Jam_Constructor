from django.forms import ModelForm
from .models import Playlist

class AddSongForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ['song']