from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status, exceptions, filters
from .models import Album, Artist, Song, Playlist, Genre, PlaylistSong
from .serializers import AlbumSerializer, ArtistSerializer, SongSerializer, PlaylistSerializer, GenreSerializer, RegisterSerializer, UserDetailSerializer
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens = get_token_for_user(user)
        return Response({
            'user': RegisterSerializer(user, context={'request': request}).data,
            'access': tokens['access'],
            'refresh': tokens['refresh'],
        }, status=status.HTTP_201_CREATED)

User = get_user_model()  
# For listing all the users
class UserListView(generics.ListAPIView):
    queryset = User.objects.all().prefetch_related('playlists')
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'first_name', 'last_name']

# For getting details about a specific user (by pk)
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all().prefetch_related('playlists')
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
'''
Album
'''
# For Creating an Album
class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all() 
    serializer_class = AlbumSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        genres = serializer.validated_data.pop("genres", None)
        album = serializer.save(owner=self.request.user)
        if genres is not None:
            album.genres.set(genres)



# For Updating an Album
class AlbumUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_update(self, serializer):
        genres = serializer.validated_data.pop("genres", None)
        album = serializer.save()
        if genres is not None:
            album.genres.set(genres)

# For deleting an Album
class AlbumDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Album.objects.all().prefetch_related("genres")
    serializer_class = AlbumSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = "pk"

'''
Artist
'''

# For Creating an Artist
class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

# For Updating an Artist
class ArtistUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_update(self, serializer):
        serializer.save()

# For deleting an Artist
class ArtistDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = "pk"
    
'''
Song
'''

# For Creating a Song
class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
  
#For Updating a Song
class SongUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_update(self, serializer):
        serializer.save()  
        
#For deleting a song
class SongDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsOwnerOrReadOnly]

'''
Playlist
'''
    
# For Creating a Playlist
class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
    
class PlaylistUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_update(self, serializer):
        serializer.save()  
        
class PlaylistDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsOwnerOrReadOnly]
      
# For adding and removing songs from a playlust  
class PlaylistSongManagerView(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    
    def post(self, request, pk):
        """This is for adding a song to a playlist"""
        playlist = get_object_or_404(Playlist, pk=pk)
        if playlist.owner != request.user:
            raise exceptions.PermissionDenied(detail="Must be teh creator of this playlist")
        
        song = get_object_or_404(Song, pk = request.data.get('song_id'))
        last = PlaylistSong.objects.filter(playlist=playlist).order_by('-order').first()
        order = request.data.get('order') or (last.order + 1 if last else 1)
        obj, created = PlaylistSong.objects.get_or_create(
            playlist=playlist, song=song, defaults={'order': order}
        )        
        if not created:
            return Response({'detail': 'Song already in playlist'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(PlaylistSerializer(playlist, context={'request': request}).data, status=status.HTTP_201_CREATED)  
    
    def delete(self, request, pk):
        """This is for removing a song from a playlist"""
        playlist = get_object_or_404(Playlist, pk=pk)
        if playlist.owner != request.user:
            raise exceptions.PermissionDenied("Must be the creator of this playlist")
        song = get_object_or_404(Song, pk=request.data.get('song_id'))
        ps = get_object_or_404(PlaylistSong, playlist = playlist, song = song)
        ps.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            


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