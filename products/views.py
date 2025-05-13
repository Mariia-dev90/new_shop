from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.db.models import Q

from .filters import ProductFilter
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny
from .documents import ProductDocument

# class ProductListView(APIView):
#     permission_classes = [AllowAny]
#
#     def get(self, request):
#         """
#         Получение списка продуктов с фильтрацией по:
#         - категории (category_id)
#         - поставщику (supplier_id)
#         - минимальной и максимальной цене (min_price, max_price)
#         - состоянию заморозки (state: 'froz' или 'not froz')
#
#         Пример:
#         /api/products/list/?category_id=2&supplier_id=5&min_price=100&max_price=500&state=froz
#         """
#
#         products = Product.objects.filter(is_active=True)
#
#         category_id = request.query_params.get("category_id")
#         supplier_id = request.query_params.get("supplier_id")
#         min_price = request.query_params.get("min_price")
#         max_price = request.query_params.get("max_price")
#         state = request.query_params.get("state")
#
#         if category_id:
#             products = products.filter(category_id=category_id)
#         if supplier_id:
#             products = products.filter(supplier_id=supplier_id)
#         if min_price:
#             products = products.filter(unit_price__gte=min_price)
#         if max_price:
#             products = products.filter(unit_price__lte=max_price)
#         if state:
#             products = products.filter(measure_state=state)
#
#         serializer = ProductSerializer(products, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)


class ProductListView(generics.ListAPIView):
    """
            Получение списка продуктов с фильтрацией по:
            - категории (category_id)
            - поставщику (supplier_id)
            - минимальной и максимальной цене (min_price, max_price)
            - состоянию заморозки (state: 'froz' или 'not froz')

            Пример:
            /api/products/list/?category_id=2&supplier_id=5&min_price=100&max_price=500&state=froz
            """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    permission_classes = [AllowAny]


class ProductSearchView(APIView):
    def get(self, request):
        """Этот эндпоинт возвращает список всех товаров в базе данных. Если добавить параметр name,
        то будет выполнен фильтр по частичному совпадению имени продукта.

        \nGET /api/products/list/search/?name=wing"""

        query = request.query_params.get('name', None)

        if query:
            es_results = ProductDocument.search().query("match", name=query).execute()
            product_ids = [hit.meta.id for hit in es_results]
            products = Product.objects.filter(id__in=product_ids, is_active=True)
        else:
            products = Product.objects.filter(is_active=True)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        # if query:
        #     products = ProductDocument.search().query("match", name=query)
        #     response = products.execute()
        #     results = [{"name": product.name} for product in response]
        # else:
        #     # Если name пустой или не передан — вернуть все товары
        #     results = [{"name": product.name} for product in Product.objects.all()]
        #
        # return Response(results, status=status.HTTP_200_OK)


