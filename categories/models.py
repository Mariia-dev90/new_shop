from django.db import models

from django.utils.translation import gettext as _




class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Parent Category")
    )
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.name}'

    def children(self):
        """Return replies of a Category."""
        return Category.objects.filter(parent=self)

    @property
    def is_parent(self):
        """Return `True` if instance is a parent."""
        return self.parent is None










#
# from mptt.models import MPTTModel, TreeForeignKey
# from django.db import models
# from django.utils.translation import gettext_lazy as _
#
#
#
# class Categoria(MPTTModel):
#     name = models.CharField(max_length=200, db_index=True)
#     parent = TreeForeignKey(
#         "self",
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         related_name="children",  # Название для связи дочерних категорий
#         verbose_name=_("Parent Category")
#     )
#     image = models.ImageField(upload_to='categories/', blank=True, null=True)
#
#     class Meta:
#         verbose_name = "Categoria"
#         verbose_name_plural = "Categorias"
#
#     def __str__(self):
#         return self.name
#
#     @property
#     def is_parent(self):
#         """Возвращает `True`, если категория имеет дочерние элементы"""
#         return self.get_children().exists()

