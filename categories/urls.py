# users/urls.py

from django.urls import path
# from django.views.decorators.cache import cache_page

from .views import CategoryList

urlpatterns = [
    path('list/', CategoryList.as_view(), name='category-list'),
    # path('list/post/', CategoryGetList.as_view(), name='category-subcategories'),  # Новый путь
]
