from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="DRSOA API",
      default_version='v1',
      description="Documentacion API",
    #   terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="marito.hidalgo94@gmail.com"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    # requisito para la doc de API de swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('documentacion-api/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('documentacion-api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    path('dj-admin/', admin.site.urls),
    # Pagina de Portada
    path('', include('core.web.urls')),
    # Panel de Adminstracion
    path('dashboart/', include('core.panel.urls')),
    # Control de Entrar
    path('login/', include('core.login.urls')),
    # Servicios Actino
    path('servicios/actino/', include('core.servicios.actino.urls')),
    # Servicios Pyra y Par
    path('servicios/pyra-par/', include('core.servicios.pyra_par.urls')),
    # Servicios SEOC API
    path('servicios/seoc/', include('core.servicios.seoc.urls')),
    # Servicios Met Api
    path('servicios/met/', include('core.servicios.met.urls')),

    # Libreria para editor de texto
    # path('ckeditor', include('ckeditor_uploader.urls')),
    path('ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Administracion GOAC"
admin.site.index_title = "Modulos del sistema"
