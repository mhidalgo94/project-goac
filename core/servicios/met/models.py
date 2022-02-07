import os
import binascii
from django.db import models
from config import settings
from django.forms import model_to_dict

class MetHistoricosModel(models.Model):
    CHOICES = (
        ('MIN','MIN'),
        ('MAX','MAX')
    )
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    fecha = models.DateTimeField(verbose_name = 'Fecha')
    variable = models.CharField( verbose_name='Variable', max_length=10)
    nombre = models.CharField(verbose_name='Nombre', max_length=50, null=True, blank=True)
    tipo = models.CharField(verbose_name='Tipo', choices=CHOICES, max_length=10)
    valor = models.FloatField(verbose_name='Valor',max_length=20)
    unidad_medida = models.CharField(verbose_name='Unidad de Medida', max_length=20, null=True, blank=True)

    def toJSON(self):
        item = model_to_dict(self, exclude=('fecha_creacion','fecha_modificacion'))
        item['fecha'] = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return item

    class Meta:
        verbose_name = 'Histórico Estación Automática'
        verbose_name_plural = 'Históricos Estación Automática'

    def __str__(self):
        return f'{self.variable}-{self.tipo}--{self.valor}'

class MetModel(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    fecha = models.DateTimeField('Fecha')
    ta = models.FloatField('ta')
    hr = models.FloatField('hr')
    vv = models.FloatField('vv')
    dv = models.FloatField('dv')
    ri = models.FloatField('ri')
    hi = models.FloatField('hi')
    rc = models.FloatField('rc')
    hc = models.FloatField('hc')
    pr = models.FloatField('pr')

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        item['hora'] = self.fecha.strftime('%H:%M:%S')
        item['datetime'] = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return item

    def __str__(self):
        return '{}'.format(self.fecha.strftime('%Y-%m-%d %H:%M:%S'))

    class Meta:
        verbose_name = 'Met'
        verbose_name_plural = 'Met'


class MetAPITokenModel(models.Model):
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
