from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .documents import ProductDocument
from .models import Product
import logging

# Настройка логирования
logger = logging.getLogger(__name__)


@receiver(post_save, sender=Product)
def update_supplier_document(sender, instance, created, **kwargs):
    try:
        ProductDocument().update(instance)

        if created:
            logger.info(
                f"✅ Product document for '{instance.name}' (ID: {instance.id}) successfully created in Elasticsearch."
            )
        else:
            logger.info(
                f"🔄 Product document for '{instance.name}' (ID: {instance.id}) was updated in Elasticsearch."
            )
    except Exception as e:
        logger.error(
            f"❌ Failed to index product '{instance.name}' (ID: {instance.id}) in Elasticsearch: {str(e)}"
        )

@receiver(post_delete, sender=Product)
def delete_supplier_document(sender, instance, **kwargs):
    try:
        # Логируем удаление документа из Elasticsearch
        logger.info(f"Deleting product document for: {instance.name} (ID: {instance.id})")

        # Удаление документа из Elasticsearch
        ProductDocument().delete(instance)

        logger.info(
            f"Product document for {instance.name} (ID: {instance.id}) successfully deleted from Elasticsearch.")
    except Exception as e:
        logger.error(f"Error while deleting product document for {instance.name} (ID: {instance.id}): {str(e)}")



# @receiver(post_save, sender=Product)
# def update_supplier_document(sender, instance, created, **kwargs):
#
#      ProductDocument().update(instance)
#
#
#
# @receiver(post_delete, sender=Product)
# def delete_supplier_document(sender, instance, **kwargs):
#     ProductDocument().delete(instance)
