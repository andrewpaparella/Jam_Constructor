from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, IntegerField, TextField
# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    year = models.IntegerField()

    def __string__(self):
        return self.name

class Playlist(models.Model):
    title = CharField(max_length=100)

    song = models.ManyToManyField(Song)
    users = models.ForeignKey(User, on_delete=models.CASCADE)

class ReviewPlaylist(models.Model):
    content = TextField(max_length=250)
    rating = IntegerField(max_length=1)

    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
