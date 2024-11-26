from  rest_framework.serializers import ModelSerializer
from  posts.models import Post

class PostSerializador(ModelSerializer):
    class Meta:
        model = Post
        fields = ["title","content","slug","miniature","created_at","published","user","categorie"]