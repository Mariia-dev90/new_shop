# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Offer

@receiver(post_save, sender=Offer)
def hide_product_on_offer(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        if product.is_active:
            product.is_active = False
            product.save()
