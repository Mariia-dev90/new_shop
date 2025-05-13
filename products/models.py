from django.db import models

from suppliers.models import Supplier

from categories.models import Category


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name




class Product(models.Model):
    MEASURE_CHOICES = [
        ('kg', 'Kilogram'),
        ('l', 'Litre'),
    ]
    STATE_CHOICES = [
        ('froz', 'Frozen'),
        ('not froz', 'Not frozen'),
    ]


    name = models.CharField(max_length=200, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True) # поменять на False
    image = models.ImageField(upload_to='products', blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')
    measure_unit = models.CharField(max_length=10, choices=MEASURE_CHOICES, db_index=True)
    measure_unit_amount = models.PositiveIntegerField(db_index=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True, null=True, blank=True)
    measure_state = models.CharField(max_length=10, choices=STATE_CHOICES, db_index=True)
    available_quantity = models.PositiveIntegerField(db_index=True)
    production_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    origin_of_product = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    is_active = models.BooleanField(default=True,null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.name}'

    @property
    def measure(self):
        return f"Packs of {self.measure_unit_amount} {self.measure_unit} {self.measure_state}"

    @property
    def available(self):
        return f"{self.available_quantity} packs"

    @property
    def price(self):
        return f"{self.unit_price} AED"


