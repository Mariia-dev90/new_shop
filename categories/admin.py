from django.contrib import admin
from django.utils.html import format_html

from .filters import CategoryListFilter
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'is_parent', 'get_image')
    search_fields = ('name',)
    # list_filter = ('parent',)
    list_filter = (CategoryListFilter,)  # Используем кастомный фильтр

    ordering = ('name',)
    def get_image(self, obj):
        # Проверяем, есть ли изображение, и возвращаем его URL с HTML-тегом img
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                               obj.image.url)
        return "No Image"

    get_image.short_description = "Image"


# from django.contrib import admin
# from mptt.admin import MPTTModelAdmin


#
# @admin.register(Categoria)
# class CategoryAdmin(MPTTModelAdmin):
#     list_display = ('id', 'name', 'parent', 'is_parent', 'get_image')
#     search_fields = ('name',)
#     # list_filter = ('parent', )
#     list_filter = (CategoriaHierarchyFilter,)
#
#     def get_image(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)
#         return "No Image"
#
#     get_image.short_description = "Image"
