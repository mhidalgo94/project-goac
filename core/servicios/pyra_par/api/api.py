import json
from rest_framework import status, generics
from rest_framework.response import Response

from core.servicios.pyra_par.models import Pyra_ParModel, PyParAPIToken
from core.servicios.pyra_par.api.serializers import PyraParSerializers

# Vista para crear los datos
class PyraParCreateApiView(generics.CreateAPIView):
    serializer_class = PyraParSerializers

    def post(self, request, token):
        """
            Debes enviar el api_key (token) del servicio mediando la url para que de permiso para crear los datos nuevos
        """
        user = PyParAPIToken.objects.filter(key = token)
        if user:
            data_serializer = self.serializer_class(data=request.data)
            if data_serializer.is_valid():
                data_serializer.save()
                return Response(data_serializer.data)
            else:
                tojson = json.dumps(data_serializer.errors)
                return Response(data_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            mensaje = {'mensaje':'No esta autorizado acceder a estos datos'}
            tojson = json.dumps(mensaje)
            return Response(mensaje, status = status.HTTP_401_UNAUTHORIZED)

# API para filtrar por rango de fecha Y-M-D
class PyraParFilterRangeDate(generics.ListAPIView):
    serializer_class = PyraParSerializers
    queryset = Pyra_ParModel.objects.all()

    def get(self, request,token, fecha_inicio= None, fecha_final= None, ):
        """
            Debes enviar el api_key (token) del servicio mediando la url para que de permiso para filtrar.
            Ingresar un fecha inicial y final para el filtrado (YYYY-MM-DD)
        """
        try:
            user = PyParAPIToken.objects.filter(key = token)
            if len(user) > 0:
                model_data = self.get_serializer().Meta.model.objects.filter(fecha__date__range = (fecha_inicio,fecha_final))
                model_serializers = self.serializer_class(model_data, many = True)
                return Response(model_serializers.data)
                
            elif len(user) == 0:
                mensaje = {'mensaje':'No esta autorizado acceder a estos datos'}
                tojson = json.dumps(mensaje)
                return Response(mensaje, status = status.HTTP_401_UNAUTHORIZED)
        except Exception as e:

            return Response({'mensaje':str(e)})

# API para filtrar solo un dia por fecha Y-M-D
class PyraParFilterDate(generics.ListAPIView):
    serializer_class = PyraParSerializers
    queryset = Pyra_ParModel.objects.all()

    def get(self, request,token, fecha= None):
        """
            Debes enviar el api_key (token) del servicio mediando la url para que de permiso para filtrar.
            Ingresar una fecha  para el filtrado (YYYY-MM-DD)
        """
        try:
            user = PyParAPIToken.objects.filter(key = token)
            if len(user) > 0:
                model_data = self.get_serializer().Meta.model.objects.filter(fecha__date = fecha)
                model_serializers = self.serializer_class(model_data, many = True)
                return Response(model_serializers.data)
                
            elif len(user) == 0:
                mensaje = {'mensaje':'No esta autorizado acceder a estos datos'}
                tojson = json.dumps(mensaje)
                return Response(mensaje, status = status.HTTP_401_UNAUTHORIZED)
        except Exception as e:

            return Response({'mensaje':str(e)})


