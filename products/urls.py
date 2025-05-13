# users/urls.py

from django.urls import path
# from django.views.decorators.cache import cache_page

from .views import ProductListView, ProductSearchView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='products-list'),
    path('list/search/', ProductSearchView.as_view(), name='product'),
    # path('list/post/', CategoryGetList.as_view(), name='category-subcategories'),  # Новый путь
]
