import re
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.servicios.pyra_par.models import Pyra_ParModel, APIToken
from core.servicios.pyra_par.api.serializers import PyraParSerializers


@api_view(['POST'])
def PyraParPostApiView(request, token):
    if request.method == 'GET':
        try:
            user = APIToken.objects.get(key = token)
            print(user)
            model_data = Pyra_ParModel.objects.all()
            model_serializers = PyraParSerializers(model_data, many = True)
            return Response(model_serializers.data)
        except:
            return Response({'mensaje':'No esta autorizado a acceder a estos datos'}, status = status.HTTP_401_UNAUTHORIZED)


    if request.method == 'POST':
        try:
            user = APIToken.objects.get(key = token)
            data_serializer = PyraParSerializers(data=request.data)
            if data_serializer.is_valid():
                data_serializer.save()
                return Response(data_serializer.data)
            return Response(data_serializer.errors)
            
        except:
            return Response({'mensaje':'No esta autorizado a acceder a estos datos'}, status = status.HTTP_401_UNAUTHORIZED)



@api_view(['GET'])
def PyraParAllList(request):

    if request.method == 'GET':
        model_data = Pyra_ParModel.objects.all()
        model_serializers = PyraParSerializers(model_data, many = True)
        return Response(model_serializers.data)

@api_view(['GET'])
def PyraParFilter(request,token, fecha= None, inicio= None, final= None):

    if request.method == 'GET':
        user = APIToken.objects.filter(key = token).first()
        if user is None:
            return Response({'mensaje':'No esta autorizado a acceder a estos datos'}, status = status.HTTP_401_UNAUTHORIZED)

        model_data = Pyra_ParModel.objects.filter(fecha = fecha, tiempo__range = [inicio, final])
        model_serializers = PyraParSerializers(model_data, many = True)
        return Response(model_serializers.data)
