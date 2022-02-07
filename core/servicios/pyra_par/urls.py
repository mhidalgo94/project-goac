from django.urls import path

from .api.api import PyraParCreateApiView,PyraParFilterRangeDate, PyraParFilterDate
from .api.api_auth import *

urlpatterns = [
    path('api/create/<str:token>/', PyraParCreateApiView.as_view()),
    path('api/filter/<str:token>/<str:fecha_inicio>/<str:fecha_final>/', PyraParFilterRangeDate.as_view()),
    path('api/filter/<str:token>/<str:fecha>/', PyraParFilterDate.as_view()),
    # Api por authenticacion
    path('api/v1/', PyraParRetrieveAuthAPIView.as_view(), name='pypar-ret-auth'),
    path('api/v1/last/', PyraParLastAuthAPIView.as_view(), name='pypar-last-auth'),
    path('api/v1/filter/', PyraParFilterDateAuthAPIView.as_view(), name='pypar-filer-datetime-auth'),
]