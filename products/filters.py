# filters.py

import django_filters
from .models import Product



class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="unit_price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="unit_price", lookup_expr='lte')
    category_id = django_filters.NumberFilter(field_name="category__id")
    supplier_id = django_filters.NumberFilter(field_name="supplier__id")
    state = django_filters.CharFilter(field_name="measure_state")
    is_active = django_filters.BooleanFilter(field_name="is_active")


    class Meta:
        model = Product
        fields = ['category_id', 'supplier_id', 'min_price', 'max_price', 'state', 'is_active']

    @property
    def qs(self):
        parent_qs = super().qs
        # Применяем is_active=True, если пользователь не указал сам
        if 'is_active' not in self.data:
            return parent_qs.filter(is_active=True)
        return parent_qs


