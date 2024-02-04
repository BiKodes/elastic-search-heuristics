"""Book register models."""
import json
from django.conf import settings
from django.db import models
from django.utils.translation import gettext, gettext_lazy as _
from book.constants import *

class Publisher(models.Model):
    """Book Publisher."""
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_county = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    latitude = models.DecimalField(null=True,
                                   blank=True,
                                   decimal_places=15,
                                   max_digits=19,
                                   default=0)
    longitude = models.DecimalField(null=True,
                                   blank=True,
                                   decimal_places=15,
                                   max_digits=19,
                                   default=0)
    
    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return self.name
    
    @property
    def location_field_indexing(self):
        """Location for indexing.
        
        It is used in Elasticsearch indexing/tests fo geo_distance native filter.
        """
        return {
            'lat': self.latitude,
            'lon': self.longitude
        }
    
class Author(models.Model):
    """Book Author."""
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    passport_photo = models.ImageField(upload_to='authors', null=True, blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return self.name

class Tag(models.Model):
    """Tag model."""
    title = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self) -> str:
        return self.title
    
class Book(models.Model):
    """Book."""
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name="books")
    Publisher = models.ForeignKey(Publisher, related_name="books", on_delete=models.CASCADE)
    publication_date = models.DateField()
    status = models.CharField(max_length=100,
                              choices=BOOK_PUBLISHING_STATUS,
                              default=BOOK_PUBLISHING_STATUS_DEFAULT)
    isbn = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pages = models.PositiveIntegerField(default=200)
    stock_count = models.PositiveIntegerField(default=20)
    tags = models.ManyToManyField(Tag, related_name='books', blank=True)

    class Meta:
        ordering = ["isbn"]

    def __str__(self) -> str:
        return self.title
    
    @property
    def publisher_indexing(self):
        """Publisher for indexing.

        Used in Elasticsearch indexing.
        """
        if self.publisher is not None:
            return self.publiser.name
        
    def tags_indexing(self):
        """Tags for indexing.
        
        Used in Elasticsearch indexing.
        """
        return [tag.title for tag in self.tags.all().iterator()]
