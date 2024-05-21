from django.contrib import admin

from playlists.models import Playlist


# admin.site.register(Playlist)
class PlaylistTabAdmin(admin.TabularInline):
    model = Playlist
    fields = "track", "created_timestamp"
    search_fields = "track", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ["user", "track_display", "created_timestamp", ]
    list_filter = ["created_timestamp", "user", "track__title", ]
#
#     def user_display(self, obj):
#         if obj.user:
#             return str(obj.user)
#         return "Анонимный пользователь"
#
    def track_display(self, obj):
        return str(obj.track.title)





