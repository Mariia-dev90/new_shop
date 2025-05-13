


from django.contrib import admin
from django.utils.html import format_html
from rangefilter.filters import NumericRangeFilter


from .models import Product, Country
from categories.filters import CategoryListFilter


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'name', 'category', 'supplier', 'get_measure', 'get_available', 'get_image', 'production_date', 'expiration_date', 'origin_of_product','get_price', 'measure_state',)
    search_fields = ('name', 'category__name', 'supplier__name')
    list_filter = (
                    CategoryListFilter,
                    'supplier',
                    'measure_state',
                    ('unit_price', NumericRangeFilter),
                    'is_active',
                    )

    def get_measure(self, obj):
        return obj.measure
    get_measure.short_description = 'Measure'

    def get_available(self, obj):
        return obj.available
    get_available.short_description = 'Available'

    def get_image(self, obj):
        # Проверяем, есть ли изображение, и возвращаем его URL с HTML-тегом img
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                               obj.image.url)
        return "No Image"

    get_image.short_description = "Image"


    def get_price(self, obj):
        return obj.price
    get_price.short_description = 'Unit price'
