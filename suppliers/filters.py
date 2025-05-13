import django_filters
from .models import Supplier

class SupplierFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')  # Фильтрация по части имени

    class Meta:
        model = Supplier
        fields = ['name']  # Укажи поля, по которым можно фильтровать
