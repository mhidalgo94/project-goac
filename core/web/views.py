import os
from core.log_error import save_log
from datetime import datetime, date
from core.talleres.models import ResumenesTallerModel, TallerModel
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from core.web.models import CatInvestigacionesModel, InvestigacionesModel, PublArtArbitrajeModel, PublEventosModel, PublReportesModel, WebModelo, InstrumentoModel, NoticiasModels
from core.miembros.models import MiembrosModel
from core.web.forms import ContactoForm
from core.servicios.actino.models import ActinoEstacionesModel, ActinoHorarioVeranoModel, ActinoObservadorModel


from config.settings import ACTINO_ROOT, STATIC_URL, ACTINO_HISTORICOS_ROOT
from core.lectura_csv import Lectura_csv


# Todas las vistas del sitio web.
class WebDetailView(ListView):
    model = WebModelo
    template_name = 'web/body.html'

    def post(self,request, *args, **kwargs):
        data ={}
        try:
            form = ContactoForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Grupo Óptica Atmosférica Camagüey'
        context['modelo'] = WebModelo.objects.last()
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        context['instrumento'] = InstrumentoModel.objects.all()
        context['noticias'] = NoticiasModels.objects.filter(estado=True).order_by('-id')[:3]
        context['form'] = ContactoForm()
        return context

# Miembros
class WebMiembroView(TemplateView):
    model = WebModelo
    template_name = 'web/miembros/miembros.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Miembros'
        context['titulo_page'] = 'Miembros del Grupo'
        context['modelo'] = WebModelo.objects.last()
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        context['miembros'] = MiembrosModel.objects.all()
        return context

class WebPerfilView(DetailView):
    template_name = 'web/miembros/perfil.html'
    queryset = MiembrosModel.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(MiembrosModel, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Perfil'
        context['titulo_page'] = 'Perfil'
        context['modelo'] = WebModelo.objects.last()
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        context['reportes'] = PublReportesModel.objects.filter(miembro__id = self.kwargs['id'], estado=True)
        context['eventos'] = PublEventosModel.objects.filter(miembro__id = self.kwargs['id'], estado=True)
        context['art_arbitrajes'] = PublArtArbitrajeModel.objects.filter(miembro__id = self.kwargs['id'], estado=True)
        context['noticias'] = NoticiasModels.objects.filter(autor__id=self.kwargs.get('id'), estado=True).order_by('-id')
        return context

# Noticias
class WebNoticiasView(TemplateView):
    model = NoticiasModels
    template_name = 'web/noticias/noticias.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request,*args, **kwargs):
        queryset = request.POST.get('buscar')
        if queryset == '':
            noticias = self.model.objects.all().order_by('-id')
        else:
            noticias = self.model.objects.filter(Q(titulo__icontains=queryset)|Q(desc__icontains=queryset)).distinct()

        titulo = 'GOAC | Noticias'
        titulo_page = 'Noticias'
        busqueda = queryset
        modelo = WebModelo.objects.last()
        nav_inv = CatInvestigacionesModel.objects.all()
        context = {
            'titulo': titulo,
            'titulo_page': titulo_page,
            'modelo': modelo,
            'nav_inv': nav_inv,
            'noticias': noticias,
            'busqueda': busqueda
        }

        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Noticias'
        context['titulo_page'] = 'Noticias'
        context['modelo'] = WebModelo.objects.last()
        context['noticias'] = self.model.objects.all().order_by('-id')
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        return context

class WebNoticiasDetailView(DetailView):
    template_name = 'web/noticias/post_noticia.html'
    queryset = NoticiasModels.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(NoticiasModels, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Noticias'
        context['modelo'] = WebModelo.objects.last()
        context['titulo_page'] = 'Noticias'
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        return context

# Publicaciones
#· Reportes
class WebReportesView(TemplateView):
    model = PublReportesModel
    template_name = 'web/publicaciones/reportes/reportes.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Reportes'
        context['titulo_page'] = 'Reportes'
        context['modelo'] = WebModelo.objects.last()
        context['reportes'] = PublReportesModel.objects.filter(estado=True)
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        return context

#· Articulos con Arbitrajes
class WebArtArbitrajesView(TemplateView):
    model = PublArtArbitrajeModel
    template_name = 'web/publicaciones/articulos_arbitrajes/art_arbitrajes.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Articulos con Arbitrajes'
        context['titulo_page'] = 'Articulos con Arbitrajes'
        context['modelo'] = WebModelo.objects.last()
        context['art_arbitrajes'] = PublArtArbitrajeModel.objects.filter(estado=True)
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        return context

#· Eventos
class WebEventosView(TemplateView):
    model = PublEventosModel
    template_name = 'web/publicaciones/eventos/eventos.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Eventos'
        context['titulo_page'] = 'Eventos'
        context['modelo'] = WebModelo.objects.last()
        context['eventos'] = PublEventosModel.objects.filter(estado=True)
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        return context

# Investigaciones
class InvestigacionesDetailView(TemplateView):
    model = InvestigacionesModel
    template_name = 'web/investigaciones/investigaciones_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Investigaciones'
        context['titulo_page'] = CatInvestigacionesModel.objects.get(nombre=self.kwargs['nombre'])
        context['info'] =  self.model.objects.filter(estado=True,cat=CatInvestigacionesModel.objects.get(nombre=self.kwargs['nombre']))
        context['modelo'] = WebModelo.objects.last()
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        return context

# Talleres
class TalleresView(TemplateView):
    model = TallerModel
    template_name = 'web/talleres/todos_talleres.html'


    def post(self, request,*args, **kwargs):
        queryset = request.POST.get('buscar')
        titulo = 'GOAC | Talleres'
        titulo_page = 'Talleres'
        busqueda = queryset
        modelo = WebModelo.objects.last()
        nav_inv = CatInvestigacionesModel.objects.all()
        info = self.model.objects.filter(Q(titulo__icontains=queryset)|Q(descripcion__icontains=queryset)).distinct()
        context = {
            'titulo': titulo,
            'titulo_page': titulo_page,
            'modelo': modelo,
            'nav_inv': nav_inv,
            'info': info,
            'busqueda': busqueda
        }
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Talleres'
        context['titulo_page'] = "Talleres de Mediciones con Lidar en Latinoamérica"
        context['info'] =  self.model.objects.all().order_by('-id')
        context['modelo'] = WebModelo.objects.last()
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        return context

class TalleresDetailView(DetailView):
    model = TallerModel
    template_name = 'web/talleres/talleres_detalles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Detalles Taller'
        context['modelo'] = WebModelo.objects.last()
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        context['resumenes'] = ResumenesTallerModel.objects.filter(taller__pk=self.kwargs.get('pk'))
        return context

class ResumenDetailView(DetailView):
    model = ResumenesTallerModel
    template_name = 'web/talleres/talleres_resumen_detalles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Detalles Resumenes'
        context['modelo'] = WebModelo.objects.last()
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        return context

# Servicios
# Actino
class ActinoView(ListView):
    model = WebModelo
    template_name = 'web/servicios/actino/actino.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def read_csv(self, estacion ,fecha=None):
        archivo = "{}{}.csv".format(estacion,fecha)
        path = os.path.join(ACTINO_ROOT, archivo)
        info = Lectura_csv(path).get_info()
        dat = Lectura_csv(path).get_dict_datos()
        datos = {'info':info, 'datos':dat}
        return datos

    def csv_hoy(self, estacion):
        archivo = datetime.today().strftime(""+estacion+"%Y%m%d.csv")
        # archivo = "D20210225.csv"
        path = os.path.join(ACTINO_ROOT, archivo)
        info = Lectura_csv(path).get_info()
        dat = Lectura_csv(path).get_dict_datos()
        datos = {'info':info, 'datos':dat}
        return datos
        
    def graficos_rad_historico(self, mes, estacion,irradiancia):
        nombre_archivo = f'{estacion}{irradiancia}.csv'
        archivo = os.path.join(ACTINO_HISTORICOS_ROOT,nombre_archivo)
        data = list()
        with open(archivo, 'r') as doc:
            datos = doc.readlines()
            array = datos[mes].split(',')
            array.remove("\n")
            for m in array:
                if m == '-999':
                    # data.append(None)
                    continue
                else:
                    data.append(float(m))
        return data

    def graficos_rad(self, datos, irradiancia):
        rad_= list()
        for m in datos:
            if int(m[irradiancia]) < 0: 
                rad_.append(None)
            else:
                rad_.append(int(m[irradiancia]))
        return rad_

    def ejeX(self, mes=None):
        if mes is None:
            mes = date.today().month
        # Horarios de 7 a 17 hora en los meses Enero Feb Oct Nov Dic
        horario_7_17 = [1,2,10,11,12]
        horario_7_18 = [3]
        horario_6_18 = [4,5,6,7,8]
        horario_6_17 = [9]
        if mes in horario_7_17:
            horario =  list(range(7,18))
            return horario
        elif mes in horario_7_18:
            horario =  list(range(7,19))
            return horario
        elif mes in horario_6_18:
            horario =  list(range(6,19))
            return horario
        elif mes in horario_6_17:
            horario =  list(range(6,18))
            return horario
        else:
            return 'Ha Ocurrido un error en el mes'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST.get('action')
            estacion =request.POST.get('estacion')
            # Basado en la fecha del dia
            if action == 'hoy':
                mes = datetime.today().month - 1

                try:
                    data['datos'] = self.csv_hoy(estacion)['datos']
                    data['info'] = self.csv_hoy(estacion)['info']
                    # Datos de Graficos Radiacion Global
                    data['grafico_global'] = self.graficos_rad(data['datos'], 'global')
                    data['grafico_global_historicos'] = self.graficos_rad_historico(mes, estacion, 'global')
                    # Datos de Graficos Radiacion Directa
                    data['grafico_directa'] = self.graficos_rad(data['datos'], 'directa')
                    data['grafico_directa_historicos'] = self.graficos_rad_historico(mes, estacion, 'directa')
                    # Datos de Graficos Radiacion Difusa
                    data['grafico_difusa'] = self.graficos_rad(data['datos'], 'difusa')
                    data['grafico_difusa_historicos'] = self.graficos_rad_historico(mes, estacion, 'difusa')
                    data['ejex_grafico'] = self.ejeX()

                    # Para consultar la imagen de la base de datos
                    try:
                        obs = ActinoObservadorModel.objects.get(id = data['info']['id'])
                        if obs:
                            data['info']['imagen'] = obs.get_imagen()
                    except Exception as e:
                        error = " "+str(e)+"(Error por falta observador en el sistema)"
                        save_log(error)
                    data['info']['imagen'] = '{}{}'.format(STATIC_URL, 'img/empty.png')
                except Exception as e:
                    error = " "+str(e)
                    save_log(error)
                    data['error'] = 'Los datos de esta fecha no existen en el servidor'

            # Buscar datos por fecha
            elif action == 'buscar_fecha':
                date = request.POST.get('fecha')
                fecha = date.replace("-","")
                mes = int(fecha[4:6]) - 1
                mes_x = int(fecha[4:6])
                try:
                    data['datos'] = self.read_csv(estacion, fecha)['datos']
                    data['info'] = self.read_csv(estacion,fecha)['info']
                    # Datos de Graficos Radiacion Global
                    data['grafico_global'] = self.graficos_rad(data['datos'], 'global')
                    data['grafico_global_historicos'] = self.graficos_rad_historico(mes, estacion, 'global')
                    # Datos de Graficos Radiacion Directa
                    data['grafico_directa'] = self.graficos_rad(data['datos'], 'directa')
                    data['grafico_directa_historicos'] = self.graficos_rad_historico(mes, estacion, 'directa')
                    # Datos de Graficos Radiacion Difusa
                    data['grafico_difusa'] = self.graficos_rad(data['datos'], 'difusa')
                    data['grafico_difusa_historicos'] = self.graficos_rad_historico(mes, estacion, 'difusa')
                    data['ejex_grafico'] = self.ejeX(mes_x)

                    # Consultar la imagen de la base de datos
                    try:
                        data['info']['imagen'] = '{}{}'.format(STATIC_URL, 'img/empty.png')
                        obs = ActinoObservadorModel.objects.get(id = data['info']['id'])
                        if obs:
                            data['info']['imagen'] = obs.get_imagen()
                    except Exception as e:
                        error = " "+str(e)
                        save_log(error)
                except Exception as e:
                    error = " "+str(e)
                    save_log(error)
                    data['error'] = 'Los datos de esta fecha no existen en el servidor'
            elif action == 'contacto':
                form = ContactoForm(request.POST)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = "Error de servidor"
        except Exception as e:
            error = " "+str(e)
            save_log(error)
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Servicios Actinométrica'
        context['titulo_page'] = 'Estación Actinométrica'
        context['modelo'] = WebModelo.objects.last()
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        context['contactos'] = ContactoForm()
        context['estaciones'] = ActinoEstacionesModel.objects.all()
        context['verano'] = ActinoHorarioVeranoModel.objects.last()
        return context