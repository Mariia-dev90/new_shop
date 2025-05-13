# users/urls.py

from django.urls import path

from .views import SupplierSearchView
urlpatterns = [

    # path('list/', SupplierListView.as_view(), name='supplier-list'),
    # path('list/filter/', SupplierListFilterView.as_view(), name='supplier-filter'),
    path('list/search/', SupplierSearchView.as_view(), name='supplier'), #elastic_search

]
