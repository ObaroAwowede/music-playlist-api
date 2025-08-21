from django.urls import path, include
from . import views


urlpatterns = [
    path('artists/', views.ArtistListCreateView.as_view(), name = "artist-list-create-view"),
    path('artists/<int:pk>/update', views.ArtistUpdateView.as_view(), name = "artist-update-view"),
    path('artists/<int:pk>/delete', views.ArtistDeleteView.as_view(), name = "artist-delete-view"),
    path('albums/', views.AlbumListCreateView.as_view(), name = 'album-list-create-view'),
    path('albums/<int:pk>/update', views.AlbumUpdateView.as_view(), name = 'album-update-view' ),
    path('albums/<int:pk>/delete', views.AlbumDeleteView.as_view(), name = 'album-delete-view'),
    path('songs/', views.SongListCreateView.as_view(), name = 'song-list-create-view'),
    path('songs/<int:pk>/update', views.SongUpdateView.as_view(), name = 'song-update-view'),
    path('songs/<int:pk>/delete', views.SongDeleteView.as_view(), name = 'song-delete-view'),
    path('genres/', views.GenreListView.as_view(), name = 'genre-list-create-view'),
    path('genres/create', views.GenreCreateView.as_view(), name = 'genre-create-view')
]