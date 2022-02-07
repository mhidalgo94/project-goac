from rest_framework import serializers
from core.servicios.pyra_par.models import Pyra_ParModel

class PyraParSerializers(serializers.ModelSerializer):

    def validate(self, data):
        fecha = data['fecha']
        ckeck_ = self.Meta.model.objects.filter(fecha = fecha)
        if ckeck_:
            raise serializers.ValidationError('Estos datos existe en la base datos. Verifique datetime sea unico en la base datos')
        return data


    class Meta:
        model = Pyra_ParModel
        exclude = ['id','fecha_creacion', 'fecha_modificacion']