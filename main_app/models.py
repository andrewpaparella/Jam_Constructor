from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, IntegerField, TextField
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date, datetime
# Create your models here.


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

    def __string__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("songs_details", kwargs={"song_id": self.id})
    

class Playlist(models.Model):
    title = CharField(max_length=100)

    song = models.ManyToManyField(Song)
    users = models.ForeignKey(User, on_delete=models.CASCADE)

class ReviewPlaylist(models.Model):
    content = TextField(max_length=250)
    rating = IntegerField(max_length=1)

    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
