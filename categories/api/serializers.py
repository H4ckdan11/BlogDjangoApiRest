from rest_framework import serializers
from categories.models import Categorie

class CategorieSerializador(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id','title','slug','published']