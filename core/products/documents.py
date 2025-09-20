from .models import Products
from django_elasticsearch_dsl.registries import registry # used to register the document
from django_elasticsearch_dsl import Document, fields, Index # used to create the document


@registry.register_document
class ProductsDocument(Document):
    class Index:
        name = 'products'  # name of the Elasticsearch index
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
        
    class Django:
        model = Products  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'id',
            'product_name',
            'product_brand',
            'product_price'
        ]