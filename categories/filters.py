

from .models import Category
from django.contrib.admin import SimpleListFilter

# class CategoryListFilter(SimpleListFilter):
#     title = 'Категории'
#     parameter_name = 'category'
#
#     def lookups(self, request, model_admin):
#         def build_choices(categories, level=0):
#             result = []
#             for cat in categories:
#                 indent = "— " * level
#                 result.append((str(cat.id), f"{indent}{cat.name}"))
#                 children = Category.objects.filter(parent=cat)
#                 if children.exists():
#                     result += build_choices(children, level + 1)
#             return result
#
#         root_categories = Category.objects.filter(parent__isnull=True)
#         return build_choices(root_categories)
#
#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(parent_id=self.value()) | queryset.filter(id=self.value())
#         return queryset



class CategoryListFilter(SimpleListFilter):
    title = 'Категории'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        """
        Строим список категорий с вложенностью для выпадающего списка
        """
        def build_choices(categories, level=0):
            result = []
            for cat in categories:
                indent = "— " * level  # Отступы для отображения вложенности
                result.append((str(cat.id), f"{indent}{cat.name}"))
                result += build_choices(cat.children(), level + 1)  # Рекурсивно добавляем дочерние категории
            return result

        top_categories = Category.objects.filter(parent__isnull=True)  # Корневые категории
        return build_choices(top_categories)

    def queryset(self, request, queryset):
        """
        При выборе категории показываем всех её потомков (дочерние и т.д.)
        """
        if self.value():
            try:
                category = Category.objects.get(id=self.value())
                return queryset.filter(id__in=category.children())
            except Category.DoesNotExist:
                return queryset.none()
        return queryset




#
#
# from django.contrib.admin import SimpleListFilter
# from .models import Categoria  # Импортируй свою модель
#
#
# class CategoriaHierarchyFilter(SimpleListFilter):
#     title = 'Категории'
#     parameter_name = 'categoria'
#
#     def lookups(self, request, model_admin):
#         """
#         Строим список категорий с вложенностью для выпадающего списка
#         """
#         def build_choices(categories, level=0):
#             result = []
#             for cat in categories:
#                 indent = "— " * level
#                 result.append((str(cat.id), f"{indent}{cat.name}"))
#                 result += build_choices(cat.get_children(), level + 1)
#             return result
#
#         top_categories = Categoria.objects.filter(parent__isnull=True)
#         return build_choices(top_categories)
#
#     def queryset(self, request, queryset):
#         """
#         При выборе категории показываем всех её потомков (дочерние и т.д.)
#         """
#         if self.value():
#             try:
#                 categoria = Categoria.objects.get(id=self.value())
#                 return queryset.filter(id__in=categoria.get_descendants())
#             except Categoria.DoesNotExist:
#                 return queryset.none()
#         return queryset
