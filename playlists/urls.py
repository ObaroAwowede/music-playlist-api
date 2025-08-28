from django.urls import path, include
from . import views


urlpatterns = [
    path('api/users/', views.UserListView.as_view(), name = 'users-list-view'),
    path('api/users/<int:pk>/', views.UserDetailView.as_view(), name = 'user-detail-view'),
    path('api/artists/', views.ArtistListCreateView.as_view(), name = "artist-list-create-view"),
    path('api/artists/<int:pk>/', views.ArtistRetrieveUpdateDeleteView.as_view(), name = "artist-retrieve-update-delete-view"),
    path('api/albums/', views.AlbumListCreateView.as_view(), name = 'album-list-create-view'),
    path('api/albums/<int:pk>/', views.AlbumRetrieveUpdateDeleteView.as_view(), name = 'album-retrieve-update-delete-view' ),
    path('api/songs/', views.SongListCreateView.as_view(), name = 'song-list-create-view'),
    path('api/songs/<int:pk>/', views.SongRetrieveUpdateDeleteView.as_view(), name = 'song-retrieve-update-delete-view'),
    path('api/playlists/', views.PlaylistListCreateView.as_view(), name = 'playlist-list-create-view'),
    path('api/playlists/<int:pk>/', views.PlaylistRetrieveUpdateDeleteView.as_view(), name = 'playlist-retrieve-update-delete-view'),
    path('api/playlists/<int:pk>/songs/', views.PlaylistSongManagerView.as_view(), name = 'playlist-manager-view'),
    path('api/genres/', views.GenreListView.as_view(), name = 'genre-list-view'),
    path('api/genres/create/', views.GenreCreateView.as_view(), name = 'genre-create-view'),
    path('api/register/', views.RegisterView.as_view(), name = 'register-view'),
]