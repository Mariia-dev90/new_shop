from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category
from .serializers import CategorySerializer, CategoryParentSerializer, CategoryRequestSerializer


# Create your views here.
class CategoryList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        """
        Получение категорий или подкатегорий по query параметру `id`.
        Если параметр `id` не передан, возвращаются только родительские категории.

        Примеры:
        - GET /api/categories/list/
        - GET /api/categories/list/?id=1
        """
        category_id = request.query_params.get("id", None)

        if category_id:
            parent_category = Category.objects.filter(id=category_id).first()
            if parent_category:
                subcategories = Category.objects.filter(parent=parent_category)
                serializer = CategorySerializer(subcategories, many=True, context={'request': request})
                return Response(serializer.data)
            else:
                return Response({"detail": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            categories = Category.objects.filter(parent=None)
            serializer = CategoryParentSerializer(categories, many=True, context={'request': request})
            return Response(serializer.data)




# class CategoryGetList(APIView):
#     permission_classes = [AllowAny]
#     serializer_class = CategoryRequestSerializer
#
#     def post(self, request):
#         """Получение категорий или подкатегорий в зависимости от переданного id. Если ничего не передает, то получаем главные категории"""
#         category_id = request.data.get("id", None)  # Получаем id из тела запроса
#
#         # Если id передано, фильтруем подкатегории по родительской категории
#         if category_id:
#             parent_category = Category.objects.filter(id=category_id).first()
#             if parent_category:
#                 subcategories = Category.objects.filter(parent=parent_category)
#                 serializer = CategorySerializer(subcategories, many=True, context={'request': request})
#                 return Response(serializer.data)
#             else:
#                 return Response({"detail": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             # Если id не передано, вернуть только родительские категории
#             categories = Category.objects.filter(parent=None)  # Родительские категории
#             serializer = CategoryParentSerializer(categories, many=True, context={'request': request})
#             return Response(serializer.data)


