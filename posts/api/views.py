from  rest_framework.viewsets import ModelViewSet
from  django_filters.rest_framework import DjangoFilterBackend
from  ..models import Post
from  .serializers import PostSerializador
from .permissions import IsAdminReadOnly

class PostApiViewSet(ModelViewSet):
    permission_classes = IsAdminReadOnly
    serializer_class = PostSerializador
    #queryset = Post.objects.all()
    queryset = Post.objects.filter(published=True)
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["title"]