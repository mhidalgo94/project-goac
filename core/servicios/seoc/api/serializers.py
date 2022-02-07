from rest_framework import serializers

from core.servicios.seoc.models import SeocModel

class SeocSerializers(serializers.ModelSerializer):

    def validate(self, data):
        tiempo = data['tiempo']
        estacion = data['estacion']
        fecha = data['fecha']
        ckeck_ = self.Meta.model.objects.filter(tiempo = data['tiempo'], estacion = data['estacion'], fecha = data['fecha'])
        if ckeck_:
            raise serializers.ValidationError('Estos datos existe en la base datos. Verifique que el tiempo sea unico correspondiente a la fecha y estacion')
        return data

    class Meta:
        model = SeocModel
        exclude = ['fecha_creacion','fecha_modificacion','id',]