import json, os
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.generics import ListAPIView

from core.servicios.met.models import MetAPITokenModel
from .serializers import MetSerializers, MetHistoricosSerializer

class MetRetrieveAuthAPIView(APIView):
    serializer_class = MetSerializers

    def get_today(self):
        # Crea un string al modelo de archvio de csv con la fecha del dia
        fecha = datetime.today().strftime("%Y-%m-%d")
        return fecha

    def validar_apikey(self,params):
        # Funcion para verficar la API_KEY
        api_key = params.get('api_key')
        user = MetAPITokenModel.objects.filter(key = api_key)
        if user:
            return True
        return False

    def validar_autenticacion(self, params):
        # Func para verificar authenticacion por user pass
        user = params.get('user')
        password = params.get('password')
        auth = authenticate(username=user, password=password)
        valid_apikey = self.validar_apikey(params)
        if auth or valid_apikey:
            return True
        return False

    def get(self, request):
        """
            Para lograr la peticion debes enviar parametros user y password o api_key para permiso.
            Este te retornara los datos del dia actual en caso q no uses fecha como parametro
        """
        params = request.query_params
        api_key  = params.get("api_key")
        try:
            validar_aut = self.validar_autenticacion(params)
            if validar_aut:
                fecha = params.get('fecha', self.get_today())
                model_data = self.serializer_class.Meta.model.objects.filter(fecha__date = fecha)
                model_serializers = self.serializer_class(model_data, many = True)
                return Response(model_serializers.data, status=status.HTTP_200_OK)
                
            else:
                mensaje = {'mensaje':'No esta autorizado acceder a estos datos'}
                return Response(mensaje, status = status.HTTP_401_UNAUTHORIZED)
        except Exception as e:

            return Response({'mensaje':str(e)})

class MetLastAuthAPIView(APIView):
    serializer_class = MetSerializers

    def get_today(self):
        # Crea un string al modelo de archvio de csv con la fecha del dia
        fecha = datetime.today().strftime("%Y-%m-%d")
        return fecha

    def validar_apikey(self,params):
        # Funcion para verficar la API_KEY
        api_key = params.get('api_key')
        user = MetAPITokenModel.objects.filter(key = api_key)
        if user:
            return True
        return False

    def validar_autenticacion(self, params):
        # Func para verificar authenticacion por user pass
        user = params.get('user')
        password = params.get('password')
        auth = authenticate(username=user, password=password)
        valid_apikey = self.validar_apikey(params)
        if auth or valid_apikey:
            return True
        return False

    def get(self, request):
        """
            Para lograr la peticion debes enviar parametros user y password o api_key para permiso.
            Retornara el ultimo valor de la fecha alctual
        """
        params = request.query_params
        api_key  = params.get("api_key")
        try:
            validar_aut = self.validar_autenticacion(params)
            if validar_aut:
                fecha = self.get_today()
                model_data = self.serializer_class.Meta.model.objects.filter(fecha__date = fecha).last()
                model_serializers = self.serializer_class(model_data)
                return Response(model_serializers.data)
                
            else:
                mensaje = {'mensaje':'No esta autorizado acceder a estos datos'}
                return Response(mensaje, status = status.HTTP_401_UNAUTHORIZED)
        except Exception as e:

            return Response({'mensaje':str(e)})

class MetFilterDatetimeAuthAPIView(APIView):
    serializer_class = MetSerializers

    def get_today(self):
        # Crea un string al modelo de archvio de csv con la fecha del dia
        fecha = datetime.today().strftime("%Y-%m-%d %H:%M")
        return fecha
    
    def validar_apikey(self,params):
        # Funcion para verficar la API_KEY
        api_key = params.get('api_key')
        user = MetAPITokenModel.objects.filter(key = api_key)
        if user:
            return True
        return False

    def validar_autenticacion(self, params):
        # Func para verificar authenticacion por user pass
        user = params.get('user')
        password = params.get('password')
        auth = authenticate(username=user, password=password)
        valid_apikey = self.validar_apikey(params)
        if auth or valid_apikey:
            return True
        return False

    def get(self, request):
        """
            Para lograr la peticion debes enviar parametros user y password o api_key para permiso.
            Debes ingresar el parametro fecha1,fecha1 para el rango del filtrado
        """
        params = request.query_params
        try:
            validar_aut = self.validar_autenticacion(params)
            if validar_aut:
                fecha1 = params.get('fecha1', self.get_today())
                fecha2 = params.get('fecha2', self.get_today())
                
                model_data = self.serializer_class.Meta.model.objects.filter(fecha__range = (fecha1,fecha2))
                model_serializers = self.serializer_class(model_data, many = True)
                return Response(model_serializers.data, status=status.HTTP_200_OK)
                
            else:
                mensaje = {'mensaje':'No esta autorizado acceder a estos datos'}
                return Response(mensaje, status = status.HTTP_401_UNAUTHORIZED)
        except Exception as e:

            return Response({'mensaje':str(e)})


class MetHistoricosAPI(ListAPIView):
    serializer_class = MetHistoricosSerializer
    queryset = serializer_class.Meta.model.objects.all()

    

