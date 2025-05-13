# suppliers/documents.py

from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Supplier








supplier_index = Index('suppliers')
supplier_index.settings(
    number_of_shards=1,
    number_of_replicas=0,
    analysis={
        "analyzer": {
            "edge_ngram_analyzer": {
                "tokenizer": "edge_ngram_tokenizer",
                "filter": ["lowercase"]
            }
        },
        "tokenizer": {
            "edge_ngram_tokenizer": {
                "type": "edge_ngram",
                "min_gram": 1,
                "max_gram": 20,
                "token_chars": ["letter"]
            }
        }
    }
)

@registry.register_document
class SupplierDocument(Document):
    name = fields.TextField(
        analyzer="edge_ngram_analyzer",
        search_analyzer="standard"
    )

    class Index:
        name = 'suppliers'
        settings = supplier_index._settings

    class Django:
        model = Supplier
        fields = []










# @registry.register_document
# class SupplierDocument(Document):
#
#
#     class Index:
#         name = 'suppliers'
#         settings = {"number_of_shards": 1, "number_of_replicas": 0}
#
#     class Django:
#         model = Supplier  # Модель, для которой создается индекс
#         fields = ['name']  # Список полей модели



