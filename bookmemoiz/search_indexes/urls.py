from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .viewsets.book import BookDocumentView

router = DefaultRouter()
books = router.register(r'book',
                        BookDocumentView,
                        basename='bookdocument')


urlpatterns = [
    url(r'^', include(router.urls)),
]
