from django.shortcuts import render
from rest_framework import generics
from .models import Album, Artist, Song, Genre, Playlist
from .serializers import AlbumSerializer, ArtistSerializer, SongSerializer, PlaylistSerializer, GenreSerializer

# For Creating an Album
class AlbumCreate(generics.ListCreateAPIView):
    queryset = Album.objects.all() 
    serializer_class = AlbumSerializer

# For Creating an Artist
class ArtistCreate(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# For Creating a Song
class SongCreate(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
# For Creating a Playlist
class PlaylistCreate(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    
# For Creating a Genre
class GenreCreate(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer