from django.contrib import admin
from .models import Categorie

# Register your models here.
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['title','slug','published']