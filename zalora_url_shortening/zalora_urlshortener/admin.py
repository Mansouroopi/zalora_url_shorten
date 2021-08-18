from django.contrib import admin

from .models import Shortener


class ShortenerAdmin(admin.ModelAdmin):
    list_display = ('long_url', 'short_url', 'created_at')
    list_filter = ('created_at',)


admin.site.register(Shortener,ShortenerAdmin)