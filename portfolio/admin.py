from django.contrib import admin
from django.contrib.admin import AdminSite

from django.urls import reverse

from .models import Series_of_photos, Photomodel, Photo, Audio

AdminSite.site_header = "Ermák's Photography"
AdminSite.site_title = "Администритивный сайт Ermák's Photography"

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

class SeriesOfPhotosAdmin(admin.ModelAdmin):
    def view_on_site(self, obj):
        url = reverse('series_of_photos', kwargs={'pk':obj.pk})
        return f'http://127.0.0.1:8000{url}'

    list_display = ("title", "get_cover_img", "city", "date")
    date_hierarchy = 'date'
    list_filter = ['city', 'photomodels']

    search_fields = ['title']

    inlines = [PhotoInline]
    filter_horizontal = ['photomodels']

admin.site.register(Series_of_photos, SeriesOfPhotosAdmin)
admin.site.register(Photomodel)
admin.site.register(Audio)