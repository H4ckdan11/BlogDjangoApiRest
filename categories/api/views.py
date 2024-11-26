from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Categorie
from .serializers import CategorieSerializador
from .permissions import IsAdminReadOnly

class CategorieApiViewSet(ModelViewSet):
    permission_classes = [IsAdminReadOnly]
    serializer_class =  CategorieSerializador
    #queryset = Categorie.objects.all()
    queryset = Categorie.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title']