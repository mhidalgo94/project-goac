from django.urls import path
from .api.api import MetCreateApiView, MetFilterRangeDate,MetFilterDate
from .api.api_auth import *


urlpatterns = [
    # Esta url solo es para insertar datos post al servidor
    path('api/create/<str:token>/', MetCreateApiView.as_view()),
    # Estas url son para los filtros por Rango de  fechas
    path('api/filter/<str:token>/<str:fecha_inicio>/<str:fecha_final>/', MetFilterRangeDate.as_view()),
    # Esta url para filtro por fecha
    path('api/filter/<str:token>/<str:fecha>/', MetFilterDate.as_view()),
    # Api por authenticacion
    path('api/v1/', MetRetrieveAuthAPIView.as_view(), name='met-ret-auth'),
    path('api/v1/last/', MetLastAuthAPIView.as_view(), name='met-last-auth'),
    path('api/v1/filter/', MetFilterDatetimeAuthAPIView.as_view(), name='met-filer-datetime-auth'),
    path('api/v1/historicos', MetHistoricosAPI.as_view(), name='methist-list-auth'),

    
]