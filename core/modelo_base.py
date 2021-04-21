from django.db import models

from django.conf import settings

# Base de todas las clases
class ModeloBase(models.Model):
    user_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_creation', null=True, blank=True)
    date_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='user_update',
    null=True, blank=True)
    user_update = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract= True

class ModeloBaseDos(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True