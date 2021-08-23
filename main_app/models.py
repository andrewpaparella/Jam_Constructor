from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date, datetime
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    year = models.PositiveIntegerField(
     validators=[
          MinValueValidator(1900),
          MaxValueValidator(datetime.now().year)
     ],
     help_text="Use the following format: YYYY")
    youtube = models.URLField(blank=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("songs_details", kwargs={"song_id": self.id})
    

class Playlist(models.Model):
    title = CharField(max_length=100)

    song = models.ManyToManyField(Song)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("playlists_details", kwargs={"playlist_id": self.id})

RATE = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)

class ReviewPlaylist(models.Model):
    content = models.TextField(max_length=250)
    rating = models.IntegerField(default=RATE[0][0], choices=RATE)
    date = models.DateField(auto_now_add=True, blank=True)

    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-date']


class ReviewSong(models.Model):
    content = models.TextField(max_length=250)
    rating = models.IntegerField(default=RATE[0][0], choices=RATE)
    date = models.DateField(auto_now_add=True, blank=True)

    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-date']