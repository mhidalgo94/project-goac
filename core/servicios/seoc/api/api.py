import json
from rest_framework.response import Response
from rest_framework import status, generics

from core.servicios.seoc.models import SeocModel, SeocAPIToken
from .serializers import SeocSerializers

# Vista para crear los datos
class SeocCreateApiView(generics.CreateAPIView):
    serializer_class = SeocSerializers

    def post(self, request, token):
        """
            Para lograr la peticion debes enviar parametros user y password o api_key para permiso.
            Este te retornara los datos del dia actual en caso q no uses fecha como parametro
        """
        user = SeocAPIToken.objects.filter(key = token)
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
class SeocFilterRangeDate(generics.ListAPIView):
    serializer_class = SeocSerializers
    queryset = SeocModel.objects.all()

    def get(self, request,token, estacion = None,fecha_inicio= None, fecha_final= None, ):
        """
            Para lograr la peticion debes enviar parametros user y password o api_key para permiso.
            Retornara el ultimo valor de la fecha alctual
        """
        try:
            user = SeocAPIToken.objects.filter(key = token)
            if len(user) > 0:
                model_data = self.get_serializer().Meta.model.objects.filter(estacion=estacion,fecha__range = (fecha_inicio,fecha_final))
                model_serializers = self.serializer_class(model_data, many = True)
                return Response(model_serializers.data)
                
            elif len(user) == 0:
                mensaje = {'mensaje':'No esta autorizado acceder a estos datos'}
                tojson = json.dumps(mensaje)
                return Response(mensaje, status = status.HTTP_401_UNAUTHORIZED)
        except Exception as e:

            return Response({'mensaje':str(e)})

# API para filtrar solo un dia por fecha Y-M-D
class SeocFilterDate(generics.ListAPIView):
    serializer_class = SeocSerializers
    queryset = SeocModel.objects.all()

    def get(self, request,token,estacion=None, fecha= None):
        """
            Para lograr la peticion debes enviar parametros user y password o api_key para permiso.
            Debes ingresar el parametro fecha1,fecha1 para el rango del filtrado
        """
        try:
            user = SeocAPIToken.objects.filter(key = token)
            if len(user) > 0:
                model_data = self.get_serializer().Meta.model.objects.filter(estacion = estacion,fecha = fecha)
                model_serializers = self.serializer_class(model_data, many = True)
                return Response(model_serializers.data)
                
            elif len(user) == 0:
                mensaje = {'mensaje':'No esta autorizado acceder a estos datos'}
                tojson = json.dumps(mensaje)
                return Response(mensaje, status = status.HTTP_401_UNAUTHORIZED)
        except Exception as e:

            return Response({'mensaje':str(e)})

