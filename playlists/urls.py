from django.urls import path, include
from . import views


urlpatterns = [
    path('users/', views.UserListView.as_view(), name = 'users-list-view'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name = 'user-detail-view'),
    path('artists/', views.ArtistListCreateView.as_view(), name = "artist-list-create-view"),
    path('artists/<int:pk>/update/', views.ArtistUpdateView.as_view(), name = "artist-update-view"),
    path('artists/<int:pk>/delete/', views.ArtistDeleteView.as_view(), name = "artist-delete-view"),
    path('albums/', views.AlbumListCreateView.as_view(), name = 'album-list-create-view'),
    path('albums/<int:pk>/update/', views.AlbumUpdateView.as_view(), name = 'album-update-view' ),
    path('albums/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name = 'album-delete-view'),
    path('songs/', views.SongListCreateView.as_view(), name = 'song-list-create-view'),
    path('songs/<int:pk>/update/', views.SongUpdateView.as_view(), name = 'song-update-view'),
    path('songs/<int:pk>/delete/', views.SongDeleteView.as_view(), name = 'song-delete-view'),
    path('playlists/', views.PlaylistListCreateView.as_view(), name = 'playlist-list-create-view'),
    path('playlists/<int:pk>/update/', views.PlaylistUpdateView.as_view(), name = 'playlist-update-view'),
    path('playlists/<int:pk>/delete/', views.PlaylistDeleteView.as_view(), name = 'playlist-delete-view'),
    path('playlists/<int:pk>/songs/', views.PlaylistSongManagerView.as_view(), name = 'playlist-manager-view'),
    path('genres/', views.GenreListView.as_view(), name = 'genre-list-view'),
    path('genres/create/', views.GenreCreateView.as_view(), name = 'genre-create-view'),
    path('api/register/', views.RegisterView.as_view(), name = 'register-view'),
]