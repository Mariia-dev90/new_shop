from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .documents import SupplierDocument
from .models import Supplier
import logging

# Настройка логирования
logger = logging.getLogger(__name__)


@receiver(post_save, sender=Supplier)
def update_supplier_document(sender, instance, created, **kwargs):
    try:
        SupplierDocument().update(instance)

        if created:
            logger.info(
                f"✅ Supplier document for '{instance.name}' (ID: {instance.id}) successfully created in Elasticsearch."
            )
        else:
            logger.info(
                f"🔄 Supplier document for '{instance.name}' (ID: {instance.id}) was updated in Elasticsearch."
            )
    except Exception as e:
        logger.error(
            f"❌ Failed to index product '{instance.name}' (ID: {instance.id}) in Elasticsearch: {str(e)}"
        )

@receiver(post_delete, sender=Supplier)
def delete_supplier_document(sender, instance, **kwargs):
    try:
        # Логируем удаление документа из Elasticsearch
        logger.info(f"Deleting Supplier document for: {instance.name} (ID: {instance.id})")

        # Удаление документа из Elasticsearch
        SupplierDocument().delete(instance)

        logger.info(
            f"Supplier document for {instance.name} (ID: {instance.id}) successfully deleted from Elasticsearch.")
    except Exception as e:
        logger.error(f"Error while deleting Supplier document for {instance.name} (ID: {instance.id}): {str(e)}")
