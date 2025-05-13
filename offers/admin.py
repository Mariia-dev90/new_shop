from django.contrib import admin
from django.db import models
from django.utils.html import format_html

from .models import Offer
from products.models import Product


# Register your models here.
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'get_minimum_quantity', 'get_price')
    search_fields = ('product__name', 'name', )
    # list_filter = ('name', )
    ordering = ('name',)


    def get_price(self, obj):
        return obj.price
    get_price.short_description = 'Sale price'

    def get_minimum_quantity(self, obj):
        return obj.minimum_quantity
    get_minimum_quantity.short_description = 'Minimum quantity'

    # Показывать только активные продукты в поле выбора
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product":
            kwargs["queryset"] = Product.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "product":
    #         # Получаем ID редактируемого объекта (Offer)
    #         obj_id = request.resolver_match.kwargs.get('object_id')
    #         if obj_id:
    #             try:
    #                 offer = Offer.objects.get(pk=obj_id)
    #                 # Добавляем текущий продукт + фильтруем только активные
    #                 kwargs["queryset"] = Product.objects.filter(
    #                     models.Q(is_active=True) | models.Q(pk=offer.product_id)
    #                 )
    #             except Offer.DoesNotExist:
    #                 kwargs["queryset"] = Product.objects.filter(is_active=True)
    #         else:
    #             kwargs["queryset"] = Product.objects.filter(is_active=True)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Сделать поле product readonly при редактировании
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Если редактируем объект — делаем product только для чтения
            return ('product',)
        return ()

    # Показываем только активные продукты при создании
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "product":
    #         if request.resolver_match.kwargs.get('object_id'):
    #             return super().formfield_for_foreignkey(db_field, request, **kwargs)
    #         kwargs["queryset"] = Product.objects.filter(is_active=True)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)


