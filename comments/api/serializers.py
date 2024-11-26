from rest_framework.serializers import ModelSerializer
from ..models import Comment

class CommentSerializador(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content","created_at","user","post"]