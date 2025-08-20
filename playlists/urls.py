from django.urls import path, include
from . import views


urlpatterns = [
    path('albums/', views.AlbumListCreateView.as_view(), name = 'album-list-create-view'),
    path('artists/', views.ArtistListCreateView.as_view(), name = "artist-list-create-view")
]