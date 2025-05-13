from rest_framework import serializers
from .models import  Offer
from  products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.CharField(source='supplier.name', read_only=True)
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

class OfferSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)


    class Meta:
        model = Offer
        fields = [
            'id',
            'name',
            'product',
            'minimum',
            'new_price',
            'price',
            'minimum_quantity',

        ]

