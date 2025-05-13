from rest_framework import serializers
from .models import Product, Country
from suppliers.models import Supplier


# class CategoryParentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Category
#         fields = ['id', 'name']

# class SupplierSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Supplier
#         fields = ['id', 'name']





class ProductSerializer(serializers.ModelSerializer):
    measure = serializers.ReadOnlyField()
    available = serializers.ReadOnlyField()
    supplier = serializers.CharField(source='supplier.name', read_only=True)
    # supplier = SupplierSerializer(read_only=True)
    origin_of_product = serializers.CharField(source='origin_of_product.name', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'image',
            # 'category',
            'supplier',
            'measure_unit',
            'measure_unit_amount',
            'unit_price',
            'measure_state',
            'available_quantity',
            'production_date',
            'expiration_date',
            'origin_of_product',
            'measure',
            'available',
        ]
