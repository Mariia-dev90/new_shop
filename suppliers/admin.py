from django.contrib import admin
from django.utils.html import format_html

from .models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image', 'description',)
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)


    def get_image(self, obj):
        # Проверяем, есть ли изображение, и возвращаем его URL с HTML-тегом img
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                               obj.image.url)
        return "No Image"

    get_image.short_description = "Image"


