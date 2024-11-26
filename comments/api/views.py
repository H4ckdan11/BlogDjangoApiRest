from  rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import  DjangoFilterBackend
from ..models import Comment
from .serializers import CommentSerializador
from .permissions import IsOwnerOrReadAndCreateOnly

class CommentApiViewSet(ModelViewSet):
    permission_classes = IsOwnerOrReadAndCreateOnly
    serializer_class = CommentSerializador
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]