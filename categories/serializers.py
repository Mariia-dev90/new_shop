

from rest_framework import serializers
from .models import Category

class CategoryParentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ['id', 'name',  'parent', 'image']


class CategoryRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()


    class Meta:
        model = Category
        fields = ['id', 'name',  'parent', 'children', 'image']


    def get_children(self, obj):
        children = obj.children()
        serializer = CategorySerializer(children, many=True, context=self.context)
        return serializer.data

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

