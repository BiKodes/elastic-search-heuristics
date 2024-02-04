from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry


@receiver(post_save)
def update_document(sender, **kwargs):
    """Update document on added/changed records.
    
    This updates Book document in related models have been updated in the database.
    """
    app_label = sender.meta.app_label
    model_name = sender._meta.model_name
    instance = kwargs['instance']

    if app_label == 'book':
        if model_name == 'publisher':
            instances = instance.book.all()
            for _instance in instances:
                registry.update(_instance)

    if model_name == 'author':
        instances = instance.book.all()
        for _instance in instances:
            registry.update(_instance)

    if model_name == 'tag':
        instances = instance.book.all()
        for _instance in instances:
            registry.update(_instance)

@receiver(post_delete)
def delete_document(sender, **kwargs):
    """Update document on deleted records.
    
    Updates Book document from index if related fields have been removed from database.
    """
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = kwargs['instance']

    if app_label == 'book':
        if model_name == 'publisher':
            instances = instance.book.all()
            for _instance in instances:
                registry.update(_instance)
    
        if model_name == 'author':
            instances = instance.book.all()
            for _instance in instances:
                registry.update(_instance)

        if model_name == 'tag':
            instances = instance.book.all()
            for _instance in instances:
                registry.update(_instance)