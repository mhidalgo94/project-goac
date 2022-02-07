from django.urls import path
from .api.views import ActinoRetrievewApiView

urlpatterns = [
    path('api/v1/', ActinoRetrievewApiView.as_view(), name="actino-retrieve"),
]