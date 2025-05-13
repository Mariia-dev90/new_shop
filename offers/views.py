from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Offer
from .serializers import OfferSerializer


# Create your views here.


class OfferListView(generics.ListAPIView):
    """
            Получение списка оферов:

            Пример:
            /api/offers/list/
            """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = ProductFilter
    permission_classes = [AllowAny]
