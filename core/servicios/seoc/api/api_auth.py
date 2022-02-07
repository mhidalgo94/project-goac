import json, os
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate

from core.servicios.seoc.models import SeocAPIToken, SeocModel
from .serializers import SeocSerializers

class SEOCRetrieveAuthAPIView(APIView):
    serializer_class = SeocSerializers

    def get_today(self):
        # Crea un string al modelo de archvio de csv con la fecha del dia
        fecha = datetime.today().strftime("%Y-%m-%d")
        return fecha

    def validar_apikey(self,params):
        # Funcion para verficar la API_KEY
        api_key = params.get('api_key')
        user = SeocAPIToken.objects.filter(key = api_key)
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
            Enviar los parametros requeridos de user, password o api_key para permisos de los datos.
            Enviar "estacion", "fecha" y "tiempo" como parametros extras, al no enviar ninguno de estos,
            tomara la estacion 355(Camaguey), y fecha y hora actual
        """
        params = request.query_params
        try:
            validar_aut = self.validar_autenticacion(params)
            if validar_aut:
                fecha = params.get('fecha', self.get_today())
                tiempo = params.get('tiempo',None)
                estacion = params.get('estacion',355)
                if tiempo is None:
                    model_data = self.serializer_class.Meta.model.objects.get(fecha=fecha,estacion=estacion)
                    model_serializers = self.serializer_class(model_data)
                    return Response(model_serializers.data, status=status.HTTP_200_OK)
                else:
                    model_data = self.serializer_class.Meta.model.objects.filter(fecha = fecha,estacion=estacion).last()
                    return Response(model_serializers.data,status=status.HTTP_200_OK)

 
            else:
                mensaje = {'mensaje':'No esta autorizado acceder a estos datos'}
                return Response(mensaje, status = status.HTTP_401_UNAUTHORIZED)
        except SeocModel.DoesNotExist:
            return Response({"mensaje":"No existe datos con esos parametos"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'mensaje':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SEOCLastAuthAPIView(APIView):
    serializer_class = SeocSerializers

    def get_today(self):
        # Crea un string al modelo de archvio de csv con la fecha del dia
        fecha = datetime.today().strftime("%Y-%m-%d")
        return fecha

    def validar_apikey(self,params):
        # Funcion para verficar la API_KEY
        api_key = params.get('api_key')
        user = SeocAPIToken.objects.filter(key = api_key)
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
            Enviar los parametros requeridos de user, password o api_key para permisos de los datos.
            Enviar "estacion" como parametros extras, al no enviar 
            tomara la estacion 355(Camaguey).
            retornara el ultimo dato de la tabla
        """
        params = request.query_params
        try:
            validar_aut = self.validar_autenticacion(params)
            if validar_aut:
                fecha = self.get_today()
                estacion = params.get('estacion',355)
                model_data = self.serializer_class.Meta.model.objects.filter(fecha = fecha,estacion=estacion).last()
                if model_data:
                    model_serializers = self.serializer_class(model_data)
                    return Response(model_serializers.data, status=status.HTTP_200_OK)
                else:
                    return Response({"mensaje":"no hay datos"}, status=status.HTTP_200_OK)
                
            else:
                mensaje = {'mensaje':'No esta autorizado acceder a estos datos'}
                return Response(mensaje, status = status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'mensaje':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SEOCFilterDateAuthAPIView(APIView):
    serializer_class = SeocSerializers

    def get_today(self):
        # Crea un string al modelo de archvio de csv con la fecha del dia
        fecha = datetime.today().strftime("%Y-%m-%d")
        return fecha
    
    def validar_apikey(self,params):
        # Funcion para verficar la API_KEY
        api_key = params.get('api_key')
        user = SeocAPIToken.objects.filter(key = api_key)
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
            Debes ingresar parametros user, password o apo_key para la authenticacion.
            Parametro de "estacion" o coge el valor por defecto 355 (Camaguey).
            Parametros de fecha1 y fecha1 para el rango del filtrado por fecha, al no 
            ingresar esos parametros va ingresar el dia actual
        """
        params = request.query_params
        try:
            validar_aut = self.validar_autenticacion(params)
            if validar_aut:
                estacion = params.get('estacion', 355)
                fecha1 = params.get('fecha1', self.get_today())
                fecha2 = params.get('fecha2', self.get_today())
                
                model_data = self.serializer_class.Meta.model.objects.filter(fecha__range = (fecha1,fecha2),estacion=estacion)
                
                if model_data:
                    model_serializers = self.serializer_class(model_data, many = True)
                    return Response(model_serializers.data, status=status.HTTP_200_OK)
                else:
                    return Response({"mensaje":"no hay datos"}, status=status.HTTP_200_OK)
                
            else:
                mensaje = {'mensaje':'No esta autorizado acceder a estos datos'}
                return Response(mensaje, status = status.HTTP_401_UNAUTHORIZED)
        except Exception as e:

            return Response({'mensaje':str(e)})
