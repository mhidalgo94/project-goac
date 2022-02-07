
import os
import json
from datetime import datetime
from core.log_error import save_log
from config.settings import LOG_ERROR_MET
from rest_framework import status
from rest_framework.response import Response

# Modelo y serializadores
from core.servicios.met.models import MetModel, MetAPITokenModel
from .serializers import MetSerializers

from rest_framework import generics

# API para crear solo metodo post al servidor
class MetCreateApiView(generics.CreateAPIView):
    serializer_class = MetSerializers

    def post(self, request, token):
        """
            Debes enviar el api_key (token) del servicio mediando la url para que de permiso para crear los datos nuevos
        """
        user = MetAPITokenModel.objects.filter(key = token)
        if user:
            data_serializer = self.serializer_class(data=request.data) # MetSerializers(data=request.data)
            if data_serializer.is_valid():
                data_serializer.save()
                return Response(data_serializer.data)
            else:
                tojson = json.dumps(data_serializer.errors)
                save_log(tojson,method= 'POST')
                return Response(data_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            mensaje = {'mensaje':'No esta autorizado acceder a estos datos'}
            tojson = json.dumps(mensaje)
            # save_log(LOG_ERROR_MET,tojson, method= 'POST')
            return Response(mensaje, status = status.HTTP_401_UNAUTHORIZED)


# API para filtrar por rango de fecha Y-M-D
class MetFilterRangeDate(generics.ListAPIView):
    serializer_class = MetSerializers
    queryset = MetModel.objects.all()

    def get(self, request,token, fecha_inicio= None, fecha_final= None, ):
        """
            Debes enviar el api_key (token) del servicio mediando la url para que de permiso para filtrar.
            Ingresar un fecha inicial y final para el filtrado (YYYY-MM-DD)
        """
        try:
            user = MetAPITokenModel.objects.filter(key = token)
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
class MetFilterDate(generics.ListAPIView):
    serializer_class = MetSerializers
    queryset = MetModel.objects.all()

    def get(self, request,token, fecha= None):
        """
            Debes enviar el api_key (token) del servicio mediando la url para que de permiso para filtrar.
            Ingresar una fecha  para el filtrado (YYYY-MM-DD)
        """
        try:
            user = MetAPITokenModel.objects.filter(key = token)
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

# Esto esta para crear log en el servidor aun en prueba
def save_log(texto, method= None):
        path_log_file = LOG_ERROR_MET
        fecha = datetime.now().strftime('%d-%m-%Y %H:%M')
        if os.path.isfile(path_log_file):
            with open(path_log_file,'a') as doc:
                doc.write("\n" + fecha+ " " + method+ " " + texto)
        else:
            with open(path_log_file,'w') as doc:
                doc.write("# Archivo log de Met\n" + fecha + method + texto)
