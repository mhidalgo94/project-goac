import os
import binascii
from django.db import models
from django.forms import model_to_dict
from django.conf import settings
from core.servicios.actino.models import ActinoEstacionesModel

class SeocModel(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    estacion = models.ForeignKey(ActinoEstacionesModel, verbose_name='Estación', on_delete=models.PROTECT)
    fecha = models.DateField('Fecha')
    tiempo = models.TimeField('Tiempo')
    dc = models.FloatField('dc')
    dw = models.FloatField('dw')
    dnt = models.FloatField('dnt')
    eoa = models.FloatField('eoa')
    eoan = models.FloatField('eoan')

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        item['tiempo'] = self.tiempo.strftime('%H:%M')
        return item

    def __str__(self):
        return '{} {} {}'.format(self.estacion, self.fecha,self.tiempo)

    class Meta:
        verbose_name = 'SEOC BAOD'
        verbose_name_plural = 'SEOC BAOD'


class SeocAPIToken(models.Model):
    created = models.DateTimeField(verbose_name = "Created", auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    key = models.CharField("Key", max_length=40, unique=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")

    def toJSON(self):
        item = model_to_dict(self)
        item['user'] = self.user.get_fullname()
        item['key'] = self.key
        item['fecha_modificacion'] = self.fecha_modificacion.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        else:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return f'{self.key} - {self.user.username}'