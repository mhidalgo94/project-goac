from django.db import models
from django.db.models.fields import NullBooleanField
from django.forms import model_to_dict
from ckeditor_uploader.fields import RichTextUploadingField
from config.settings import MEDIA_URL, STATIC_URL


# Create your models here.
class ActinoEstadosEstacionesModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name='Estado de la Estación', max_length=40)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name= 'Estado Estación Actino'
        verbose_name_plural = 'Estados Estaciones de Actino'

class ActinoEstacionesModel(models.Model):
    codigo = models.IntegerField('codigo', primary_key=True, unique=True)
    estacion = models.CharField(verbose_name='Estación', max_length=50)
    tipo = models.CharField(verbose_name='Tipo', max_length=10)
    imagen = models.ImageField(verbose_name="Imagen Estación",upload_to='servicios/actino/estaciones/%Y/%m/%d/' ,null=True, blank=True)
    provincia = models.CharField(verbose_name='Provincia', max_length=40)
    longitud = models.DecimalField(verbose_name='Longitud', max_digits=20, decimal_places=3)
    latitud = models.DecimalField(verbose_name='Latitud', max_digits=20, decimal_places=3)
    altura = models.DecimalField(verbose_name='Altura', default=0, decimal_places=2, max_digits=20)
    estado = models.ForeignKey(ActinoEstadosEstacionesModel, verbose_name='Estado de la Estación', on_delete=models.CASCADE)

    def get_imagen(self):
        if self.imagen:
           return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
    
    def toJSON(self):
        item = model_to_dict(self)
        item['imagen'] = self.get_imagen()
        item['estado'] = self.estado.nombre
        return item 

    class Meta:
        verbose_name= 'Estación Actino'
        verbose_name_plural = 'Estaciones de Actino'

    def __str__(self):
        return '{}:{}'.format(self.estacion, self.codigo)

class ActinoHorarioVeranoModel(models.Model):
    id = models.AutoField(primary_key=True)
    horario_verano = models.BooleanField(verbose_name='Horario Verano', default=False)


    class Meta:
        verbose_name= 'Control Actino'
        verbose_name_plural = 'Controle de Actino' 

# Modelo de los Observadores
class ActinoObservadorModel(models.Model):
    id = models.CharField('id', primary_key=True, max_length=40)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    nombre = models.CharField(verbose_name='Nombre', max_length=60,null=True, blank=True)
    estacion = models.CharField(verbose_name='Estacion', max_length=150, null=True, blank=True)
    imagen = models.ImageField(verbose_name='Imagen',upload_to='servicios/actino/observadores/%Y/%m/%d', null=True, blank=True)

    def get_imagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/miembro.png')

    def toJSON(self):
        item = model_to_dict(self)
        item['imagen'] = self.get_imagen()
        return item

    def __str__(self):
        return '{}-{}'.format(self.nombre, self.id)

    class Meta:
        verbose_name= 'Observador'
        verbose_name_plural = 'Observadores'


