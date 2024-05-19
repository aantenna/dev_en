from django.contrib import admin

from tracks.models import Categories, Tracks

# admin.site.register(Categories)
# admin.site.register(Tracks)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Tracks)
class TracksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
