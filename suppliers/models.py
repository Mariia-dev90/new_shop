from django.db import models




class Supplier(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    description = models.CharField(max_length=500, db_index=True, blank=True, null=True)
    image = models.ImageField(upload_to='suppliers/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'