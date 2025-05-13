

from rest_framework import serializers
from .models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField()

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'image']


    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
