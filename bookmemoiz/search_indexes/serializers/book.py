import json

from rest_framework import serializers
from  django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from documents.books import BookDocument

class BookDocumentSerializer(BookDocument):
    """Serializer for the Book document."""

    class Meta:
        document = BookDocument

        fields = (
            "id",
            "title",
            "description",
            "summary",
            "publisher",
            "publication_date",
            "status",
            "isbn",
            "price",
            "pages",
            "stock_count",
            "tags",
        )