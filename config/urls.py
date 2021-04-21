from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Pagina de Portada
    path('', include('core.web.urls')),
    # Panel de Adminstracion
    path('dashboart/', include('core.panel.urls')),
    # Control de Entrar
    path('login/', include('core.login.urls')),
    # Servicios Actino
    path('servicios/', include('core.servicios.actino.urls')),
    # Servicios Pyra y Par
    path('servicios/pyra-par/', include('core.servicios.pyra_par.urls')),
    # Libreria para editor de texto
    path('ckeditor', include('ckeditor_uploader.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Administracion GOAC"
admin.site.index_title = "Modulos del sistema"
