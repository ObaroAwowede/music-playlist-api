from rest_framework import serializers
from .models import Album,Artist,Song,Genre,Playlist,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class AlbumSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        required=False
    )
    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ('owner',)

class SongSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Song
        fields = '__all__'
        
class ArtistSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Artist
        fields = '__all__'
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        
class PlaylistSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    song_count = serializers.SerializerMethodField()
    size = song_count
    songs = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Playlist
        fields = ('id', 'title','songs','description','owner','song_count', 'size')
        
    def get_song_count(self, obj):
        return obj.songs.count()
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email')
        )
        return user
    
class UserDetailSerializer(serializers.ModelSerializer):
    playlists = PlaylistSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'playlists')