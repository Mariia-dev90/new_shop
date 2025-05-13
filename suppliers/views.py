from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .filters import SupplierFilter
from .models import Supplier
from .serializers import SupplierSerializer



from .documents import SupplierDocument
# class SupplierListView(APIView):
#     # Указываем фильтр в настройках класса
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = SupplierFilter
#
#     def get(self, request):
#         """Этот эндпоинт возвращает список всех поставщиков в базе данных. Если добавить параметр name,
# то будет выполнен фильтр по частичному совпадению имени поставщика. Это полезно для поиска поставщиков по части их имени.
# \nGET /api/suppliers/list/
# \nGET /api/suppliers/list/?name=Coc"""
#
#
#         suppliers = Supplier.objects.all()  # Получаем всех поставщиков
#
#         # Применяем фильтрацию
#         filterset = SupplierFilter(request.query_params, queryset=suppliers)  # Фильтрация данных по query params
#         if filterset.is_valid():  # Проверка, если фильтрация успешна
#             suppliers = filterset.qs  # Применяем отфильтрованный queryset
#         else:
#             return Response({'detail': 'Invalid filter parameters'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # Сериализуем отфильтрованные данные
#         serializer = SupplierSerializer(suppliers, many=True, context={'request': request})
#         return Response(serializer.data)



# class SupplierListFilterView(generics.ListAPIView):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = SupplierFilter
#     permission_classes = [AllowAny]



class SupplierSearchView(APIView):
    def get(self, request):
        """Этот эндпоинт возвращает список всех поставщиков в базе данных. Если добавить параметр name,
        то будет выполнен фильтр по частичному совпадению имени поставщика. Это полезно для поиска поставщиков по части их имени.
        \nGET /api/suppliers/list/search/
        \nGET /api/suppliers/list/search/?name=Coc"""

        query = request.query_params.get('name', None)

        if query:
            es_results = SupplierDocument.search().query("match", name=query).execute()
            supplier_ids = [hit.meta.id for hit in es_results]
            suppliers = Supplier.objects.filter(id__in=supplier_ids)
        else:
            suppliers = Supplier.objects.all()

        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





        # if query:
        #     suppliers = SupplierDocument.search().query("match", name=query)
        #     response = suppliers.execute()
        #     results = [{"name": supplier.name} for supplier in response]
        # else:
        #     # Если нет query параметра, то возвращаем все
        #     results = [{"name": supplier.name} for supplier in Supplier.objects.all()]
        #
        # return Response(results, status=status.HTTP_200_OK)

