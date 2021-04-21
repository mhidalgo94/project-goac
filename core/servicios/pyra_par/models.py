from django.db import models
from django.forms import model_to_dict
import binascii
import os
from django.conf import settings

# Create your models here.

class Pyra_ParModel(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    fecha = models.DateField('Fecha')
    tiempo = models.TimeField('Tiempo', unique=True)
    pyra = models.FloatField('Pyra')
    par = models.FloatField('Par')

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        return item

    def __str__(self):
        return '{} - {}'.format(self.fecha.strftime("%Y-%m-%d"), self.tiempo)

    class Meta:
        verbose_name = 'Pyra y Par'
        verbose_name_plural = 'Pyra y Par'

class APIToken(models.Model):
    created = models.DateTimeField(verbose_name = "Created", auto_now_add=True)
    key = models.CharField("Key", max_length=40, unique=True, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='auth_token', on_delete=models.CASCADE, verbose_name="User")

    def toJSON(self):
        item = model_to_dict(self)
        item['user'] = self.user.get_fullname()
        item['key'] = self.key
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