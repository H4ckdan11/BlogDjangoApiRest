from rest_framework.routers import DefaultRouter
from categories.api.views import CategorieApiViewSet

router_categorie = DefaultRouter()

router_categorie.register(prefix="categories", basename="categories", viewset=CategorieApiViewSet)