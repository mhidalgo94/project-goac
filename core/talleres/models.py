from django.db import models
from django.forms import model_to_dict
from datetime import date
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class ParticipantesTallerModel(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    nombre = models.CharField(verbose_name='Nombre', max_length=150)
    centro = models.CharField(verbose_name='Centro Pertenece', max_length=200)
    pais  = models.CharField(verbose_name='Pais', max_length=50)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return '{}   {}   {}'.format(self.nombre, self.centro, self.pais)

    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'


class TallerModel(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    titulo = models.CharField(verbose_name='Titulo Taller', max_length=150)
    fecha_inicio = models.DateField('Fecha de Inicio')
    fecha_culmina = models.DateField('Fecha de Culminación')
    descripcion = models.TextField(max_length=800, verbose_name='Descripción', null=True, blank=True)
    genesis = RichTextUploadingField(null=True,blank=True)
    programa = RichTextUploadingField(null=True,blank=True)
    participantes = models.ManyToManyField(ParticipantesTallerModel, verbose_name='Participantes', blank=True)

    def verificar_tiempo(self):
        verif = self.fecha_culmina > date.today()
        return verif
    
    def toJSON(self):
        item = model_to_dict(self,exclude='participantes')
        return item
    
    def get_titulo(self):
        return self.titulo

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Taller'
        verbose_name_plural = 'Talleres'

class ResumenesTallerModel(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    titulo = models.CharField(verbose_name='Titulo Resumen', max_length=200)
    resumen = RichTextUploadingField(null=True,blank=True)
    taller = models.ManyToManyField(TallerModel, verbose_name='Resumenes de Taller',blank=True)
    participantes = models.ManyToManyField(ParticipantesTallerModel, verbose_name='Participantes', blank=True)

    def toJSON(self):
        item = model_to_dict(self,exclude='participantes')
        item['taller'] =  [g.titulo for g in self.taller.all() ]
        return item


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Resumen Taller'
        verbose_name_plural = 'Resumenes de Talleres'