from django.db import models
from django.forms import model_to_dict
import datetime
from core.modelo_base import ModeloBaseDos
from core.miembros.choices import gender_choices, estado
from config.settings import MEDIA_URL, STATIC_URL


# Sociedad Cientifica
class SCientificaModel(ModeloBaseDos):
    nombre = models.CharField(verbose_name='Nombre Sociedad Científica', max_length=255)
    url = models.URLField(verbose_name='URL Sociedad Científica', null=True, blank=True)
    desc = models.TextField(verbose_name='Sociedad Científica', max_length=300, null=True, blank=True)

    def toJSON(self):
        item = model_to_dict(self, exclude='estados')
        return item

    class Meta:
        verbose_name= 'Sociedad Cientica'
        verbose_name_plural = 'Sociedad Cienticas'
        db_table = 'sociedad_cientifica'

    def __str__(self):
        return self.nombre


# Miembros
class MiembrosModel(ModeloBaseDos):
    estado = models.CharField(max_length=40, choices=estado, default='Activos', verbose_name='Sexo')
    nombre = models.CharField(verbose_name='Nombre', max_length=250)
    apellidos = models.CharField(verbose_name='Apellidos', max_length=250, null=True, blank=True)
    imagen = models.ImageField(verbose_name='Imagen',upload_to='miembros/%Y/%m/%d', null=True, blank=True)
    correo = models.EmailField('Correo', null=True, blank=True)
    telefono = models.CharField('Teléfono', max_length=14, null=True, blank=True)
    fech_nacido = models.DateField(verbose_name='Fecha de nacimiento', null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')
    biografia = models.TextField(verbose_name='Biografía', max_length=800, null=True, blank=True)
    ocupacion = models.CharField(verbose_name='Ocupación', max_length=100, null=True, blank=True)
    t_trabajo = models.DateField(verbose_name='Fecha de Ingreso', null=True, blank=True)
    scientifca = models.ManyToManyField(SCientificaModel, verbose_name='Sociedad Científica', blank=True)
    curriculo = models.URLField('Currículo DOC', blank=True, null=True)


    def get_imagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def full_name(self):
        return "{} {}".format(self.nombre, self.apellidos)

    def tiempo_trabajo(self):
        if self.t_trabajo is not None and self.t_trabajo!="":
            t = self.t_trabajo
            hoy = datetime.date.today()
            dias = hoy - t
            result = {}
            dias = int(dias.days)
            if dias > 30:
                mes = divmod(dias,30)
                result['mes'] = mes[0]
                result['dias'] = mes[1]
                if mes[0] > 0:
                    anio = divmod(mes[0],12)
                    result['anio'] = anio[0]
                    result['mes'] = anio[1]
                else:
                    result['dias'] = dias 
                    result['mes'] = mes                   
            else:
                result['dias'] = dias
                result['mes'] = 0
                result['anio'] = 0

            return result
        else:
            return 'Vacio'   

    def toJSON(self):
        item = model_to_dict(self, exclude=['estados', 'scientifca',])
        item['imagen'] = self.get_imagen()
        item['nombre'] = self.full_name()
        return item

    class Meta:
        verbose_name= 'Miembro'
        verbose_name_plural = 'Miembros'

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)


