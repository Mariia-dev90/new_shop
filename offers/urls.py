from django.urls import path
from .views import OfferListView

urlpatterns = [
    path('list/', OfferListView.as_view(), name='products-list'),

]
