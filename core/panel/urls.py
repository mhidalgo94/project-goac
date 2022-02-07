from django.urls import path

from .views.views import DashboartListView, ServiciosListView, EjectView
from .views.portada.views import PortadaCreateView, PortadaListView
from .views.instrumento.views import InstrumentoCreateView, InstrumentoListView, InstrumentoUpdateView
from .views.contactos.views import ContactoListView
from .views.miembros.views import MiembrosListView, MiembrosCreateView, MiembrosUpdateView, PefilMiembroEditView
from .views.miembros.scientifica.views import SCientificasListView, SCientificaCreateView, SCientificaUpdateView
from core.panel.views.noticias.views import NoticiasCreateView, NoticiasListView, NoticiasUpdateView
from core.panel.views.publicaciones.views import *
from core.panel.views.usuarios.views import *
from core.panel.views.investigaciones.views import *
from core.panel.views.talleres.participantes.views import *
from core.panel.views.talleres.resumenes.views import * 
from core.panel.views.talleres.views import *
from core.panel.views.servicios.actino.views import * 
from core.panel.views.servicios.pyra_par.views import *
from core.panel.views.servicios.seoc.views import *
from core.panel.views.servicios.met.views import *


# Path de direcciones
urlpatterns = [
    path('', DashboartListView.as_view() ,name='panel'),
    path('ejecutar/', EjectView.as_view() ,name='ejecutar'),
    # Portada Web
    path('web/edit_portada/', PortadaListView.as_view() ,name='edit_portada'),
    path('web/create_portada/', PortadaCreateView.as_view() ,name='create_portada'),
    # instrumentos
    path('web/list_instrumento/', InstrumentoListView.as_view() ,name='list_instrumento'),
    path('web/create_instrumento/', InstrumentoCreateView.as_view() ,name='create_instrumento'),
    path('web/edit_instrumento/<int:pk>/', InstrumentoUpdateView.as_view() ,name='edit_instrumento'),
    # Noticias
    path('web/list_noticias/', NoticiasListView.as_view() ,name='list_noticias'),
    path('web/create_noticias/', NoticiasCreateView.as_view() ,name='create_noticias'),
    path('web/edit_noticias/<int:pk>/', NoticiasUpdateView.as_view() ,name='edit_noticias'),
    #Contactos
    path('web/list_contacto/', ContactoListView.as_view() ,name='list_contacto'),
    # Miembros
    path('miembros/list_miembros/', MiembrosListView.as_view() ,name='list_miembros'),
    path('miembros/create_miembros/', MiembrosCreateView.as_view() ,name='create_miembros'),
    path('miembros/edit_miembros/<int:pk>/', MiembrosUpdateView.as_view() ,name='edit_miembros'),
    path('miembros/perfil_miembros/', PefilMiembroEditView.as_view() ,name='perfil_miembros'),
    # Sociedad Cientifica Miembros
    path('miembros/list_scientifica/', SCientificasListView.as_view() ,name='list_scientifica'),
    path('miembros/create_scientifica/', SCientificaCreateView.as_view() ,name='create_scientifica'),
    path('miembros/edit_scientifica/<int:pk>/', SCientificaUpdateView.as_view() ,name='edit_scientifica'),
    # Publicaciones Reportes
    path('publicaciones/reportes/list_reportes/', PublReportesListView.as_view() ,name='list_reportes'),
    path('publicaciones/reportes/create_reportes/', PublReportesCreateView.as_view() ,name='create_reportes'),
    path('publicaciones/reportes/edit_reportes/<int:pk>/', PublReportesUpdateView.as_view(),name='edit_reportes'),
    # Publicaciones Articulos y Arbitrajes
    path('publicaciones/arbitraje/list_arbitraje/', PublArtArbitrajeListView.as_view() ,name='list_arbitraje'),
    path('publicaciones/arbitraje/create_arbitraje/', PublArtArbitrajeCreateView.as_view() ,name='create_arbitraje'),
    path('publicaciones/arbitraje/edit_arbitraje/<int:pk>/', PublArtArbitrajeUpdateView.as_view(),name='edit_arbitraje'),
    # Publicaciones Eventos
    path('publicaciones/eventos/list_eventos/', PublEventosModelListView.as_view() ,name='list_eventos'),
    path('publicaciones/eventos/create_eventos/', PublEventosModelCreateView.as_view() ,name='create_eventos'),
    path('publicaciones/eventos/edit_eventos/<int:pk>/', PublEventosUpdateView.as_view(),name='edit_eventos'),
    # Investigaciones
    path('investigaciones/list_investigaciones/', InvestigacionesListView.as_view() ,name='list_investigaciones'),
    path('investigaciones/create_investigaciones/', InvestigacionesCreateView.as_view() ,name='create_investigaciones'),
    path('investigaciones/edit_investigaciones/<int:pk>/', InvestigacionUpdateView.as_view(),name='edit_investigacion'),
    # Categorias de Investigaciones
    path('investigaciones/categorias/list_categorias/', CategoriasInvListView.as_view() ,name='list_categorias'),
    # Talleres
    path('talleres/list_talleres/', TallerListView.as_view() ,name='list_talleres'),
    path('talleres/create_talleres/', TallerCreateView.as_view() ,name='create_talleres'),
    path('talleres/edit_talleres/<int:pk>/', TallerUpdateView.as_view() ,name='edit_talleres'),
    # Participantes de Talleres
    path('talleres/participantes/list_participantes/', ParticipanteTListView.as_view() ,name='list_participantes'),
    path('talleres/participantes/create_participantes/', ParticipanteTCreateView.as_view() ,name='create_participantes'),
    path('talleres/participantes/edit_participantes/<int:pk>/', ParticipanteTUpdateView.as_view() ,name='edit_participantes'),
    # Resumenes
    path('talleres/resumenes/list_resumenes/', ResumenesTListView.as_view() ,name='list_resumenes'),
    path('talleres/resumenes/create_resumenes/', ResumenesTCreateView.as_view() ,name='create_resumenes'),
    path('talleres/resumenes/edit_resumenes/<int:pk>/', ResumenesTUpdateView.as_view() ,name='edit_resumenes'),
    # Todos los servicios
    path('servicios/', ServiciosListView.as_view() ,name='todos_servicios'),
    # Servicio Actino
    path('servicios/actino/list_observadores/', ObservadoresListView.as_view() ,name='list_observadores'),
    path('servicios/actino/list_archivos/', ArchivosActinoView.as_view() ,name='list_archivos'),
    path('servicios/actino/errores/', ActinoErrorView.as_view() ,name='log_error'),
    path('servicios/actino/estaciones/', ActinoControlEstacionesView.as_view() ,name='control_estaciones'),
    path('servicios/actino/estaciones/crear_estacion/', ActinoEstacionCreateView.as_view() ,name='create_estacion'),
    path('servicios/actino/estaciones/edit_estacion/<str:codigo>/', ActinoEstacionUpdateView.as_view() ,name='edit_estacion'),
    # Servicio Pyra y Par
    path('servicios/pyra_par/list_datos_pyra_par/', PyraParDatosListView.as_view(), name= 'list_pyra_par'),
    path('servicios/pyra_par/editToken/', PyParAPITokenListView.as_view(), name= 'pypar_editToken'),
    # Servicio SEOC
    path('servicios/seoc/list_datos_seoc/', SeocDatosListView.as_view(), name= 'list_seoc'),
    path('servicios/seoc/editToken/', SeocAPITokenList.as_view(), name= 'seoc_editToken'),
    path('servicios/seoc/edit-seoc/<int:pk>/', SeocUpdateView.as_view(), name= 'seoc_edit_data'),
    # Servicio Met
    path('servicios/met/list_datos_met/', MetDatosListView.as_view(), name= 'list_met'),
    path('servicios/met/historicos_met/', MetHistoricosListView.as_view(), name= 'list_met_historicos'),
    path('servicios/met/edit-historicos_met/<int:pk>/', MetHistoricosUpdateView.as_view(), name= 'edit_historicos'),
    path('servicios/met/editToken/', MetAPITokenList.as_view(), name= 'met_editToken'),
    path('servicios/met/log-error/', MetErrorView.as_view(), name= 'met_error'),
    path('servicios/met/edit-met/<int:pk>/', MetUpdateView.as_view(), name= 'met_edit_data'),

    
    # Usuarios
    path('usuarios/list_usuarios/', UsuariosListView.as_view() ,name='list_usuarios'),
    path('usuarios/create_usuarios/', UsuariosCreateView.as_view() ,name='create_usuario'),
    path('usuarios/edit_usuarios/<int:pk>/', UsuariosUpdateView.as_view(),name='edit_usuario'),
    # Perfil Usuario
    path('usuarios/edit_perfil/', PerfilUpdateView.as_view() ,name='edit_perfil'),
    path('usuarios/edito_pwd/', PefilEditPwdView.as_view() ,name='edit_psw'),

]