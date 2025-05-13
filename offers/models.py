from django.db import models

from products.models import Product


# Create your models here.





class Offer(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='offers')
    minimum = models.PositiveIntegerField()
    new_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.product.name}'

    @property
    def price(self):
        return f"{self.new_price} AED"

    @property
    def minimum_quantity(self):
        return f"{self.minimum} packs"

