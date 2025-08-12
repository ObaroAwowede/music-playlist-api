from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    
    def _str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length = 100)
    bio = models.TextField()
    
    def __str__(self):
        return self.name
    
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    release_date = models.DateField()
    album_length = models.TimeField()
    genre = models.TextField()
    
    def __str__(self):
        return self.title
    
class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    genre = models.TextField()
    duration = models.TimeField()
    
    def __str__(self):
        return self.title

class Playlist(models.Model):
    title = models.CharField(max_length = 100)
    song = models.ManyToManyField(Song)
    description = models.TextField()
    size = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.title