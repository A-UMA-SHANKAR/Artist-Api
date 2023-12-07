
# artist_app/admin.py

from django.contrib import admin
from .models import Artist, Work

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__username')  # Add search functionality
    filter_horizontal = ('work',)  # Add a widget for ManyToManyField

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('link', 'work_type')
    list_filter = ('work_type',)  # Add filtering by work type
    search_fields = ('link',)  # Add search functionality
