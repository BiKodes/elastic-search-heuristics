"""Documents."""
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from motors.models import Car, Manufacturer, Advert
from elasticsearch_dsl import Index


manufacturer = Index('manufacturer')

manufacturer.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@registry.register_document
class Manufacturer(Document):
    class Django:
        model = Manufacturer
        fields = [
            'name',
            'country_code',
        ]


@registry.register_document
class CarDocument(Document):
    manufacturer = fields.ObjectField(properties={
        'name': fields.TextField(),
        'country_code': fields.TextField(),
    })
    adverts = fields.NestedField(properties={
        'description': fields.TextField(),
        'title': fields.TextField(),
        'pk': fields.IntegerField(),
    })
    # add a string field to the Elasticsearch mapping called type, the
    # value of which is derived from the model's type_to_string attribute
    type = fields.TextField(attr="type_to_string")

    class Index:
        name = "cars"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }

    class Django:
        model = Car
        fields = [
            'name',
            'color',
            'description',
            'year'
        ]
        # To ensure the Car will be re-saved when Manufacturer or Ad is updated
        related_models = [Manufacturer, Advert]

    @classmethod
    def generate_id(cls, car):
        return car.name

    def get_queryset(self):
        """Meant to improves performance."""
        return super(CarDocument, self).get_queryset(
            ).select_related(
                'manufacturer'
            ).prefetch_related(
                'adverts'
            )
    
    def get_instances_from_related(self, related_instance):
        """This enables the index to be updated multiple times."""
        if isinstance(related_instance, Manufacturer):
            return related_instance.car_set.all()
        elif isinstance(related_instance, Advert):
            return related_instance.car

