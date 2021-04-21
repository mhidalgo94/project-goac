
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from core.web.views import ActinoView, ResumenDetailView, TalleresDetailView, TalleresView, WebArtArbitrajesView, WebDetailView, WebEventosView, WebMiembroView, WebNoticiasDetailView, WebNoticiasView, WebPerfilView, WebReportesView, InvestigacionesDetailView

# Include your urls

urlpatterns = [
    # Portada
    path('', WebDetailView.as_view(), name='portada'),
    # Miembros
    path('miembros/', WebMiembroView.as_view(), name='miembros'),
    path('miembros/<int:id>/',WebPerfilView.as_view(),name='perfil_miembros'),
    # Noticias
    path('noticias/', WebNoticiasView.as_view(), name='noticias'),
    path('noticias/<int:id>/',WebNoticiasDetailView.as_view(),name='ver_noticias'),
    # Publicaciones Reportes
    path('publicaciones/reportes/',WebReportesView.as_view(),name='reportes'),
    # Publicaciones Reportes
    path('publicaciones/eventos/',WebEventosView.as_view(),name='eventos'),
    # Publicaciones Reportes
    path('publicaciones/art_arbitrajes/',WebArtArbitrajesView.as_view(),name='art_arbitrajes'),
    # Investigaciones
    path('investigaciones/<str:nombre>/',InvestigacionesDetailView.as_view(),name='det_investigaciones'),
    # Talleres
    path('talleres/todos_talleres/',TalleresView.as_view(),name='todos_talleres'),
    path('talleres/detalles_talleres/<int:pk>/',TalleresDetailView.as_view(),name='detalles_talleres'),
    path('talleres/detalles_resumenes/<int:pk>/',ResumenDetailView.as_view(),name='detalles_resumenes_talleres'),
    # Servicios
    # Actino
    path('servicios/actino/',ActinoView.as_view(),name='servicio_actino' ),
    
    


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

