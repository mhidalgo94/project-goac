from django.urls import path

from .api.api import PyraParPostApiView,PyraParFilter ,PyraParAllList

urlpatterns = [
    path('api/list/post/<str:token>/', PyraParPostApiView),
    # path('api/list/<str:token>/<str:fecha>/<str:inicio>/<str:final>/', PyraParFilter),
    # path('api/list/<str:token>/<str:fecha>/', PyraParFilter),
    # path('api/list/', PyraParAllList),
]