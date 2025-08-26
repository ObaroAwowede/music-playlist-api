from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.conf import settings

class User(AbstractUser):
    def __str__(self):
        return self.username

class Genre(models.Model):
    name = models.CharField(max_length= 50, unique = True)
    
    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length = 100)
    bio = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="artists",
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name
    
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    release_date = models.DateField(default = date.today)
    album_length = models.DurationField()
    genres = models.ManyToManyField(Genre)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="albums",
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.title
    
class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    release_date = models.DateField(default = date.today)
    title = models.CharField(max_length = 100)
    genres = models.ManyToManyField(Genre)
    duration = models.DurationField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="songs",
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.title

class Playlist(models.Model):
    title = models.CharField(max_length = 100)
    songs = models.ManyToManyField(Song, through='PlaylistSong')
    description = models.TextField()
    size = models.IntegerField(default = 0)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="playlists",
        null=True,
        blank=True
    )

    
    
    def __str__(self):
        return self.title
    
class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE,  related_name='playlist_songs')
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    order = models.IntegerField()
    class Meta:
        unique_together = ('playlist', 'song')
        ordering = ['order']

    def __str__(self):
        return f"{self.song.title} in {self.playlist.title}"