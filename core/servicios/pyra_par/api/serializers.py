from rest_framework import serializers
from core.servicios.pyra_par.models import Pyra_ParModel

class PyraParSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pyra_ParModel
        fields = '__all__'
        # exclude = ['fecha_creacion', 'fecha_modificacion']