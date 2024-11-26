from django.contrib import admin
from django.urls import path, include
# Agregamos la libreria de drf-yasg.
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# Importaciones de los router de las app
from categories.api.router import router_categorie
from posts.api.router import router_post
from comments.api.router import router_comment

# Creamos la funcion del schema del drf-yasg.
schema_view = get_schema_view(
   openapi.Info(
      title="Blog API Documentation",
      default_version='v1',
      description="Documentacion de nuestra API Blog.",
      terms_of_service="",
      contact=openapi.Contact(email="h4ckdan@h4cknet.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('users.api.router')),
    path('api/', include(router_categorie.urls)),
    path('api/', include(router_post.urls)),
    path('api/', include(router_comment.urls)),
]
