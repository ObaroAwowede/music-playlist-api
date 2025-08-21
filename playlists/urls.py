from django.urls import path, include
from . import views


urlpatterns = [
    path('artists/', views.ArtistListCreateView.as_view(), name = "artist-list-create-view"),
    path('artists/<int:pk>/update', views.ArtistUpdateView.as_view(), name = "artist-update-view"),
    path('albums/', views.AlbumListCreateView.as_view(), name = 'album-list-create-view'),
    path('albums/<int:pk>/delete', views.AlbumRetrieveDeleteView.as_view(), name = 'album-delete-view'),
    path('albums/<int:pk>/update', views.AlbumUpdateView.as_view(), name = 'album-update-view' ),
    path('genres/', views.GenreListCreateView.as_view(), name = 'genre-list-create-view'),
]