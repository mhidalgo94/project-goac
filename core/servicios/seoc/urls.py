from django.urls import path
from .api.api import SeocCreateApiView, SeocFilterRangeDate, SeocFilterDate
from .api.api_auth import *

urlpatterns = [
    # Url para crear datos seoc 
    path('api/create/<str:token>/',SeocCreateApiView.as_view() ),
    # Urls para filtrar por fecha y estacion
    path('api/filter/<str:token>/<int:estacion>/<str:fecha_inicio>/<str:fecha_final>/', SeocFilterRangeDate.as_view()),
    path('api/filter/<str:token>/<int:estacion>/<str:fecha>/', SeocFilterDate.as_view()),
    # Api por authenticacion
    path('api/v1/', SEOCRetrieveAuthAPIView.as_view(), name='seoc-ret-auth'),
    path('api/v1/last/', SEOCLastAuthAPIView.as_view(), name='seoc-last-auth'),
    path('api/v1/filter/date/', SEOCFilterDateAuthAPIView.as_view(), name='seoc-filer-date-auth'),
]