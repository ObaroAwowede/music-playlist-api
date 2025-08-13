from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Album, Artist, Genre, Playlist, Song, User


User = get_user_model()
admin.site.register(User, UserAdmin)

admin.site.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "artist", "release_date")
    search_fields = ("title", "artist__name")
    list_filter = ("artist")
admin.site.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    search_fields = ("name",)
admin.site.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("id","title","artist","release_date")
    search_fields = ("title","artist__name","album__title")
admin.site.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    search_fields = ("name")
admin.site.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "size")
    search_fields = ("title", "user__username")