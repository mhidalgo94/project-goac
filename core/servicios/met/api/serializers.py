from django.db.models import Max
from django.db.models.aggregates import Variance
from rest_framework import serializers

from core.servicios.met.models import MetModel, MetHistoricosModel


class MetSerializers(serializers.ModelSerializer):

    # Esta funcion es para la validacion de los historicos de la 
    # Estacion Automatica
    def comparando_historicos(self,data):
        # Verificar si el data es mayor historico vv
        qry_vv = MetHistoricosModel.objects.get(variable='vv',tipo='MAX')
        if qry_vv.valor < data['vv']:
            qry_vv.valor = data['vv']
            qry_vv.fecha = data['fecha']
            qry_vv.save()

        # Verificar si el data es mayor y menor historico ta 
        qry_ta_max = MetHistoricosModel.objects.get(variable='ta', tipo='MAX') # Consultar valor max ta
        if qry_ta_max.valor < data['ta']:
            qry_ta_max.valor = data['ta']
            qry_ta_max.fecha = data['fecha']
            qry_ta_max.save()
        qry_ta_min = MetHistoricosModel.objects.get(variable='ta',tipo='MIN') # Consultr valor min ta
        if qry_ta_min.valor > data['ta']:
            qry_ta_min.valor = data['ta']
            qry_ta_min.fecha = data['fecha']
            qry_ta_min.save()

        # Verificar si el data es mayor y menor historico hr 
        qry_hr_max = MetHistoricosModel.objects.get(variable='hr', tipo='MAX') # Consultar valor max hr
        if qry_hr_max.valor < data['hr']:
            qry_hr_max.valor = data['hr']
            qry_hr_max.fecha = data['fecha']
            qry_hr_max.save()
        qry_hr_min = MetHistoricosModel.objects.get(variable='hr',tipo='MIN') # Consultar valor min hr
        if qry_hr_min.valor > data['hr']:
            qry_hr_min.valor = data['hr']
            qry_hr_min.fecha = data['fecha']
            qry_hr_min.save()

        # Verificar si el data es mayor historico pr
        qry_pr_max = MetHistoricosModel.objects.get(variable='pr', tipo='MAX') # Consultar valor max pr
        if qry_pr_max.valor < data['pr']:
            qry_pr_max.valor = data['pr']
            qry_pr_max.fecha = data['fecha']
            qry_pr_max.save()
        qry_pr_min = MetHistoricosModel.objects.get(variable='pr',tipo='MIN') # Consultar valor min pr
        if qry_pr_min.valor > data['pr']:
            qry_pr_min.valor = data['pr']
            qry_pr_min.fecha = data['fecha']
            qry_pr_min.save()

        # Verificar si el data es mayor historico ri
        qry_ri_max = MetHistoricosModel.objects.get(variable='ri',tipo='MAX')
        if qry_ri_max.valor < data['ri']:
            qry_ri_max.valor = data['ri']
            qry_ri_max.fecha = data['fecha']
            qry_ri_max.save()
            
        # Verificar si el data es mayor hitorico hi
        qry_hi_max = MetHistoricosModel.objects.get(variable='hi', tipo='MAX')
        if qry_hi_max.valor < data['hi']:
            qry_hi_max.valor = data['hi']
            qry_hi_max.fecha = data['fecha']
            qry_hi_max.save()
        

    def validate(self, data):
        self.comparando_historicos(data)
        fecha = data['fecha']
        ckeck_ = self.Meta.model.objects.filter(fecha = fecha)
        if ckeck_:
            raise serializers.ValidationError('Estos datos existe en la base datos. Verifique datetime sea unico en la base datos')
        return data

    class Meta:
        model = MetModel
        exclude = ['id','fecha_creacion','fecha_modificacion',]


class MetHistoricosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MetHistoricosModel
        exclude = ['id','fecha_creacion','fecha_modificacion',]