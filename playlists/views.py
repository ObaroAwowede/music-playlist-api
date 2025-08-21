from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Album, Artist, Song, Playlist, Genre
from .serializers import AlbumSerializer, ArtistSerializer, SongSerializer, PlaylistSerializer, GenreSerializer

'''
Album
'''
# For Creating an Album
class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all() 
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        genres = serializer.validated_data.pop("genres", None)
        album = serializer.save(owner=self.request.user)
        if genres is not None:
            album.genres.set(genres)



# For Updating an Album
class AlbumUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_update(self, serializer):
        genres = serializer.validated_data.pop("genres", None)
        album = serializer.save()
        if genres is not None:
            album.genres.set(genres)

# For deleting an Album
class AlbumDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Album.objects.all().prefetch_related("genres")
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"

'''
Artist
'''

# For Creating an Artist
class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

# For Updating an Artist
class ArtistUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_update(self, serializer):
        serializer.save()

# For deleting an Artist
class ArtistDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"
    
'''
Song
'''

# For Creating a Song
class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
  
#For Updating a Song
class SongUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_update(self, serializer):
        serializer.save()  
        
#For deleting a song
class SongDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]

'''
Playlist
'''
    
# For Creating a Playlist
class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
    
class PlaylistUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_update(self, serializer):
        serializer.save()  
        
class PlaylistDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]
        
# For Listing a genre

class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]
    
# For Creating a genre (only admin)
class GenreCreateView(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAdminUser]

# For Deleting and Updating a genre (only admin)
class GenreRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]