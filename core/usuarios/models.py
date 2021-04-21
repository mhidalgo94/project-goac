from django.db import models
from django.forms import model_to_dict
from django.contrib.auth.models import AbstractUser

from .choices import gender_choices
from core.modelo_base import ModeloBase

from config.settings import MEDIA_URL, STATIC_URL
from core.miembros.models import MiembrosModel

# Create your models here.
class Usuarios(AbstractUser):
    imagen = models.ImageField(verbose_name='Imagen',upload_to='usuarios/%Y/%m/%d', null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')
    miembro = models.ForeignKey(MiembrosModel, on_delete=models.SET_NULL, null=True, blank=True)

    def get_fullname(self):
        return '{} {}'.format(self.first_name, self.last_name )

    def get_imagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'groups', 'user_permissions'])
        item['id'] = self.id
        if self.miembro:
            item['miembro'] = self.miembro.get_imagen()#self.miembro.full_name()
        else:
            item['miembro'] = "Sin Vinculo"
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        else:
            item['last_login'] = 'No ha accedido'
        item['imagen'] = self.get_imagen()
        item['full_name'] = '{} {}'.format(self.first_name, self.last_name)
        return item


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

