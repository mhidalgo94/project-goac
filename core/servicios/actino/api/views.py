import json, os
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from core.lectura_csv import Lectura_csv


from django.contrib.auth import authenticate

class ActinoRetrievewApiView(APIView):
    """
        Requistos para peticiones. Debes enviar el user, password.
        Tambien puedes hacer filtrados por fecha y variable de la estacion
    """

    def get_today_datetime_file(self):
        # Crea un string al modelo de archvio de csv con la fecha del dia
        fecha = datetime.today().strftime("%Y%m%d")
        return fecha

    def get_csv_fecha(self,params):
        # Si no se envia las fecha en los parametros coje la del dia por defecto
        fecha = params.get('fecha',self.get_today_datetime_file()) 
        # Si no se envia la variable de la estacion, por defecto toma la variable de camaguey
        estacion = params.get('estacion','D')
        # Nombre del archivo q hace lectura en la carpeta del actino
        file = estacion+fecha+".csv"
        return file


    def validar_autenticacion(self, params):
        user = params.get('user')
        password = params.get('password')
        auth = authenticate(username=user, password=password)
        return auth

    def get(self,request):
        params = request.query_params # toma los parametros de la url
        valir_auth = self.validar_autenticacion(params) # Verificar la authenticacion

        if valir_auth:
            file = self.get_csv_fecha(params)
            path_file = os.path.join(settings.ACTINO_ROOT, file)
            read_csv = Lectura_csv(path=path_file) # Hace lectura del csv
            try:
                # data es un dict de los datos del header y datos restantes del csv
                head= read_csv.get_info()
                head["estacion"] = estacion = params.get('estacion','D')
                datos = read_csv.get_dict_datos()
                data = dict(head=head,datos=datos)
                return Response(data,status=status.HTTP_200_OK)
            except FileNotFoundError:
                # En caso q no existe el archivo en la carpeta del csv de actino
                return Response({'error':'No existen datos de esta fecha en el servidor',}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                # En caso de algun error desconocido
                return Response({"error":"Error de servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"error":"No esta autorizado a los datos"},status=status.HTTP_401_UNAUTHORIZED)
        # si no envia los parametros correctos
        return Response({"warning":"Envie los parametros requeridos al servidor"}, status=status.HTTP_400_BAD_REQUEST)