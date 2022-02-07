from datetime import datetime
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import model_to_dict

from core.modelo_base import ModeloBaseDos
from core.miembros.models import MiembrosModel

from config.settings import MEDIA_URL, STATIC_URL

# Instrumentos
class InstrumentoModel(ModeloBaseDos):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    imagen = models.ImageField('Imagen Instrumento',upload_to='web/img/instrumento/' ,null=True, blank=True)
    desc = models.TextField(verbose_name='Descripcion Instumento', max_length=400, null=True, blank=True)
    contenido = RichTextUploadingField()


    def get_imagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def toJSON(self):
        item = model_to_dict(self)
        item['imagen'] = self.get_imagen()
        return item

    class Meta:
        verbose_name = 'Instrumento'
        verbose_name_plural = 'Instrumentos'

# Sitio Web
class WebModelo(ModeloBaseDos):
    # Para el header
    logo = models.ImageField('Imagen Logotipo',upload_to='web/img/logos' ,null=True, blank=True)
    img_banner = models.ImageField('Imagen Banner',upload_to='web/img/banner/' ,null=True, blank=True)
    titulo_banner = models.CharField('Titulo Banner', max_length=250)
    frase = models.TextField('Frase', max_length=300)

    # Estructura
    nosotros = models.TextField('Nosotros', max_length=1000)
    direccion = models.CharField('Direccion', max_length=250)
    postal = models.CharField('Postal', max_length=250)
    telefono = models.CharField('Telefono', max_length=12)
    correo = models.EmailField('Correo',null=True)
    url_facebook = models.URLField('Facebook', blank=True, null=True)
    url_Instagram = models.URLField('Instagram', blank=True, null=True)
    url_Twitter = models.URLField('Twitter', blank=True, null=True)
    footer_copyright = models.CharField('Footer', max_length=250)

    class Meta:
        verbose_name = 'web'
        verbose_name_plural = 'web'

    def __str__(self):
        return self.titulo_banner


# Contactos
class ContactoModel(ModeloBaseDos):
    nombre = models.CharField("Nombre Completo", max_length=200)
    subject = models.CharField('Titulo', max_length=200)
    correo = models.EmailField('Correo', max_length=250)
    mensaje = models.TextField('Mensaje', max_length=800)

    def toJSON(self):
        item = model_to_dict(self, exclude='estados')
        return item

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Conctactos'

    def __str__(self):
        return self.nombre

# Modelo de las Noticias
class NoticiasModels(ModeloBaseDos):
    estado = models.BooleanField('Estado', default = False)
    titulo = models.CharField(verbose_name='Titulo Publicacion', max_length=150)
    desc = models.TextField(verbose_name='Descripcion de la Publicacion', max_length=250)
    imagen = models.ImageField(verbose_name='Imagen Noticia',null=True, blank=True, upload_to='web/noticias/img/%Y/%m/%d')
    contenido = RichTextUploadingField()
    autor = models.ForeignKey(MiembrosModel, on_delete=models.CASCADE)
    doc = models.URLField('Documento', blank=True, null=True)

    def get_imagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    # Solo para el data table
    def get_file(self):
        if self.doc:
            path = self.doc
            icon = '{}{}'.format(STATIC_URL, 'img/file-download.svg')
            return [path,icon]
        else:
            path = ''
            icon = '{}{}'.format(STATIC_URL, 'img/question-circle.svg')
            return [path,icon]
    
    def get_url_file(self):
        if self.doc:
            return self.doc
        return '{}{}'.format(STATIC_URL, 'img/file-download.png')

    def toJSON(self):
        item = model_to_dict(self)
        item['autor'] = self.autor.full_name()
        item['imagen'] = self.autor.get_imagen()
        item['doc'] = self.get_file()
        return item

    def __str__(self):
        return self.titulo

# Publicacion Reportes Articulos y Eventos
class PublReportesModel(ModeloBaseDos):
    estado = models.BooleanField('Estado', default = False)
    texto = models.TextField(verbose_name='Titulo', max_length=900)
    doc = models.URLField('Documento', blank=True, null=True)
    miembro = models.ManyToManyField(MiembrosModel, verbose_name='Miembros', blank=True)
    anio = models.PositiveIntegerField(verbose_name='Año',default=datetime.now().year)
    invest = models.ForeignKey('InvestigacionesModel',verbose_name='Investigación', null=True,blank=True, on_delete=models.SET_NULL)


    # Solo para el data table
    def get_file(self):
        if self.doc:
            path = self.doc
            icon = '{}{}'.format(STATIC_URL, 'img/file-download.svg')
            return [path,icon]
        else:
            path = ''
            icon = '{}{}'.format(STATIC_URL, 'img/question-circle.svg')
            return [path,icon]

    def get_url_file(self):
        if self.doc:
            return self.doc
        return '{}{}'.format(STATIC_URL, 'img/file-download.png')

    def toJSON(self):
        item = model_to_dict(self)
        item['miembro'] = [{'nombre':g.nombre, 'imagen': g.get_imagen()} for g in self.miembro.all() ]
        item['doc'] = self.get_file()
        return item

    def __str__(self):
        return self.texto

class PublArtArbitrajeModel(ModeloBaseDos):
    estado = models.BooleanField('Estado', default = False)
    texto = models.TextField(verbose_name='Titulo', max_length=900)
    doc = models.URLField('Documento', blank=True, null=True)
    miembro = models.ManyToManyField(MiembrosModel, verbose_name='Miembros', blank=True)
    anio = models.PositiveIntegerField(verbose_name='Año',default=datetime.now().year)
    invest = models.ForeignKey('InvestigacionesModel',verbose_name='Investigación', null=True,blank=True, on_delete=models.SET_NULL)

    # Solo para el data table
    def get_file(self):
        if self.doc:
            path = self.doc
            icon = '{}{}'.format(STATIC_URL, 'img/file-download.svg')
            return [path,icon]
        else:
            path = ''
            icon = '{}{}'.format(STATIC_URL, 'img/question-circle.svg')
            return [path,icon]
    
    def toJSON(self):
        item = model_to_dict(self)
        item['miembro'] = [{'nombre':g.nombre, 'imagen': g.get_imagen()} for g in self.miembro.all() ]
        item['doc'] = self.get_file()
        return item
    
    def get_url_file(self):
        if self.doc:
            return '{}'.format( self.doc)
        return '{}{}'.format(STATIC_URL, 'img/file-download.png')


    def __str__(self):
        return self.texto

class PublEventosModel(ModeloBaseDos):
    estado = models.BooleanField('Estado', default = False)
    texto = models.TextField(verbose_name='Titulo', max_length=900)
    doc = models.URLField('Documento', blank=True, null=True)
    miembro = models.ManyToManyField(MiembrosModel, verbose_name='Miembros', blank=True)
    anio = models.PositiveIntegerField(verbose_name='Año',default=datetime.now().year)
    invest = models.ForeignKey('InvestigacionesModel',verbose_name='Investigación', null=True,blank=True, on_delete=models.SET_NULL)

    # Solo para el data table
    def get_file(self):
        if self.doc:
            path = self.doc
            icon = '{}{}'.format(STATIC_URL, 'img/file-download.svg')
            return [path,icon]
        else:
            path = ''
            icon = '{}{}'.format(STATIC_URL, 'img/question-circle.svg')
            return [path,icon]
    
    def toJSON(self):
        item = model_to_dict(self)
        item['miembro'] = [{'nombre':g.nombre, 'imagen': g.get_imagen()} for g in self.miembro.all() ]
        item['doc'] = self.get_file()
        return item
    
    def get_url_file(self):
        if self.doc:
            return '{}'.format(self.doc)
        return '{}{}'.format(STATIC_URL, 'img/file-download.png')

    def __str__(self):
        return self.texto


# Investigaciones
class CatInvestigacionesModel(ModeloBaseDos):
    nombre = models.CharField(verbose_name='Categoria Investigaciones', max_length=80)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.nombre


class InvestigacionesModel(ModeloBaseDos):
    titulo = models.CharField(verbose_name='Titulo Investigacion', max_length=310)
    cat = models.ForeignKey(CatInvestigacionesModel, verbose_name='Categoria', on_delete=models.CASCADE)
    texto = models.TextField(verbose_name='Texto', max_length=900)
    resumen = RichTextUploadingField(null=True,blank=True)
    doc = models.URLField(verbose_name='Documento', null=True, blank=True)
    miembro = models.ManyToManyField(MiembrosModel, verbose_name='Miembros', blank=True)
    anio_inicial = models.PositiveIntegerField(verbose_name='Año Inicial',default=datetime.now().year)
    anio_final = models.PositiveIntegerField(verbose_name='Año Final',default=datetime.now().year+1,)

    # Solo para el data table
    def get_file(self):
        if self.doc:
            path = self.doc
            icon = '{}{}'.format(STATIC_URL, 'img/file-download.svg')
            return [path,icon]
        else:
            path = ''
            icon = '{}{}'.format(STATIC_URL, 'img/question-circle.svg')
            return [path,icon]

    def get_url_file(self):
        if self.doc:
            return '{}'.format(self.doc)
        return '{}{}'.format(STATIC_URL, 'img/file-download.png')

    def toJSON(self):
        item = model_to_dict(self)
        item['miembro'] = [{'nombre':g.nombre, 'imagen': g.get_imagen()} for g in self.miembro.all() ]
        item['cat'] = self.cat.nombre
        item['doc'] = self.get_file()
        return item

    def __str__(self):
        return self.titulo
