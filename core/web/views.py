import os
from core.log_error import save_log
from datetime import datetime, date, timedelta
from django.db.models import Q, Sum, Max
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, TemplateView
from core.web.models import *
from core.miembros.models import MiembrosModel
from core.web.forms import ContactoForm
from core.talleres.models import *
from core.servicios.actino.models import *
from core.servicios.met.models import MetHistoricosModel, MetModel
from core.servicios.pyra_par.models import Pyra_ParModel
from core.servicios_control import leer_estado_servicios, escribir_estado_servicios

from config.settings import ACTINO_ROOT, STATIC_URL, ACTINO_HISTORICOS_ROOT, LOG_ERROR_ACTINO
from core.lectura_csv import Lectura_csv

from core.servicios.seoc.models import SeocModel


from core.salida_puesta_sol import salida_puesta

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

# Instrumentos Detalles 
class WebInstrumentoDetailView(DetailView):
    template_name = 'web/instrumento/detail_instrumento.html'
    queryset = InstrumentoModel.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(InstrumentoModel, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Instrumento'
        context['modelo'] = WebModelo.objects.last()
        context['titulo_page'] = 'Instrumento'
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')
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
        context['activos'] = MiembrosModel.objects.filter(estado="Activo")
        context['precedentes'] = MiembrosModel.objects.filter(estado="Precedente")
        context['colaboradores'] = MiembrosModel.objects.filter(estado="Colaborador")
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')

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
        context['reportes'] = PublReportesModel.objects.filter(miembro__id = self.kwargs['id'], estado=True).order_by('-anio')
        context['eventos'] = PublEventosModel.objects.filter(miembro__id = self.kwargs['id'], estado=True).order_by('-anio')
        context['art_arbitrajes'] = PublArtArbitrajeModel.objects.filter(miembro__id = self.kwargs['id'], estado=True).order_by('-anio')
        context['noticias'] = NoticiasModels.objects.filter(autor__id=self.kwargs.get('id'), estado=True).order_by('-id')
        return context

# Noticias
class WebNoticiasView(ListView):
    model = NoticiasModels
    template_name = 'web/noticias/noticias.html'
    context_object_name = 'noticia'
    queryset = NoticiasModels.objects.filter(estado=True).order_by('-id')
    paginate_by = 8

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request,*args, **kwargs):
        queryset = request.POST.get('buscar')
        if queryset == '':
            noticia = self.model.objects.filter(estado=True).order_by('-id')
        else:
            noticia = self.model.objects.filter(Q(titulo__icontains=queryset)|Q(desc__icontains=queryset)|Q(contenido__icontains=queryset)).distinct()

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
            'noticia': noticia,
            'busqueda': busqueda,
            'noticias': NoticiasModels.objects.filter(estado=True).order_by('-id'),

        }

        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Noticias'
        context['titulo_page'] = 'Noticias'
        context['modelo'] = WebModelo.objects.last()
        context['noticias'] = NoticiasModels.objects.filter(estado=True).order_by('-id')
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
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')

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
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')

        return context

#· Articulos con Arbitrajes
class WebArtArbitrajesView(TemplateView):
    model = PublArtArbitrajeModel
    template_name = 'web/publicaciones/articulos_arbitrajes/art_arbitrajes.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Articulos con Arbitraje'
        context['titulo_page'] = 'Artículos con Arbitraje'
        context['modelo'] = WebModelo.objects.last()
        context['art_arbitrajes'] = PublArtArbitrajeModel.objects.filter(estado=True)
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')

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
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')

        return context

# Investigaciones
class InvestigacionesListView(TemplateView):
    model = InvestigacionesModel
    template_name = 'web/investigaciones/investigaciones_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Investigaciones'
        context['titulo_page'] = CatInvestigacionesModel.objects.get(nombre=self.kwargs['nombre'])
        context['info'] =  self.model.objects.filter(estado=True,cat__nombre=CatInvestigacionesModel.objects.get(nombre=self.kwargs['nombre'])).order_by('-anio_inicial')
        context['modelo'] = WebModelo.objects.last()
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')

        return context

class InvestigacionesDetailView(DetailView):
    model = InvestigacionesModel
    template_name = 'web/investigaciones/investigaciones_det.html'

    def get_object(self):
        id_ = self.kwargs['id']
        cat_ = self.kwargs['nombre']
        obj = self.model.objects.filter(cat__nombre=cat_, estado=True )
        return get_object_or_404(obj, id=int(id_))
    
    def get_rel(self, obj):    
        data = obj.objects.filter(invest__cat__nombre=self.kwargs['nombre'])
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Detalles de Investigaciones'
        context['titulo_page'] = CatInvestigacionesModel.objects.get(nombre=self.kwargs['nombre'])
        context['modelo'] = WebModelo.objects.last()
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')
        context['rel_art'] = self.get_rel(PublArtArbitrajeModel)
        context['rel_even'] = self.get_rel(PublEventosModel)
        context['rel_rep'] = self.get_rel(PublReportesModel)
        
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
            'busqueda': busqueda,
            'noticias': NoticiasModels.objects.filter(estado=True).values('id')

        }
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Talleres'
        context['titulo_page'] = "Talleres de Mediciones con Lidar en Latinoamérica"
        context['info'] =  self.model.objects.all().order_by('-fecha_inicio')
        context['modelo'] = WebModelo.objects.last()
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')

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
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')

        return context

class ResumenDetailView(DetailView):
    model = ResumenesTallerModel
    template_name = 'web/talleres/talleres_resumen_detalles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Detalles Resumenes'
        context['modelo'] = WebModelo.objects.last()
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')

        return context

# Servicios
# Actino
class ActinoView(ListView):
    model = WebModelo
    template_name = 'web/servicios/actino/index_actino.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        try:
            servicios_estado = leer_estado_servicios()
            if servicios_estado['actino'] is False:
                return redirect('servicio_interrupto')
        except FileNotFoundError:
            escribir_estado_servicios({'actino': False, 'met': False, 'seoc': False, 'pyra_par': False})
            return redirect('servicio_interrupto')
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
            estacion =request.POST.get('estacion')
            action = request.POST.get('action')
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
                        data['info']['imagen'] = '{}{}'.format(STATIC_URL, 'img/miembro.png')
                        obs = ActinoObservadorModel.objects.get(id = data['info']['id'])
                        if obs:
                            data['info']['imagen'] = obs.get_imagen()
                    except Exception as e:
                        error = " "+str(e)+"(Error por falta observador en el sistema)"
                        save_log(LOG_ERROR_ACTINO,error)
                except Exception as e:
                    error = " "+str(e)
                    save_log(LOG_ERROR_ACTINO,error)
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
                        data['info']['imagen'] = '{}{}'.format(STATIC_URL, 'img/miembro.png')
                        obs = ActinoObservadorModel.objects.get(id = data['info']['id'])
                        if obs:
                            data['info']['imagen'] = obs.get_imagen()
                    except Exception as e:
                        error = " "+str(e)
                        save_log(LOG_ERROR_ACTINO,error)
                except Exception as e:
                    error = " "+str(e)
                    save_log(LOG_ERROR_ACTINO,error)
                    data['error'] = 'Los datos de esta fecha no existen en el servidor'
            elif action == 'contacto':
                form = ContactoForm(request.POST)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            elif action == "map_estaciones":
                data = []
                estaciones = ActinoEstacionesModel.objects.all()
                for m in estaciones:
                    data.append(m.toJSON())

            else:
                data['error'] = "Error de servidor"

        except Exception as e:
            error = " "+str(e)
            save_log(LOG_ERROR_ACTINO, error)
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Servicio Diagnóstico Radiación Solar Para Cuba'
        context['titulo_page'] = 'Servicio Diagnóstico Radiación Solar para Cuba'
        context['modelo'] = WebModelo.objects.last()
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        context['contactos'] = ContactoForm()
        context['estaciones'] = ActinoEstacionesModel.objects.all()
        context['verano'] = ActinoHorarioVeranoModel.objects.last()
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')

        return context

# SEOC
class SeocView(TemplateView):
    '''
    Esta vista es donde esta montado el sistema de BAOD con los graficos diarios y mensuales
    '''
    template_name = 'web/servicios/seoc/index_seoc.html'
    model = SeocModel

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        try:
            servicios_estado = leer_estado_servicios()
            if servicios_estado['seoc'] is False:
                return redirect('servicio_interrupto')
        except FileNotFoundError:
            escribir_estado_servicios({'actino': False, 'met': False, 'seoc': False, 'pyra_par': False})
            return redirect('servicio_interrupto')
        return super().dispatch(request, *args, **kwargs)

    # Saber si es bisiesto el anio
    def es_bisiesto(self, anio: int):
        return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
    # Calcular cuantos dias tiene el mes
    def obtener_dias_del_mes(self,mes: int, anio: int) -> int: 
        # Abril, junio, septiembre y noviembre tienen 30
        if int(mes) in [4, 6, 9, 11]:
            return 30
        # Febrero depende de si es o no bisiesto
        if int(mes) == 2:
            if self.es_bisiesto(int(anio)):
                return 29
            else:
                return 28
        else:
            # En caso contrario, tiene 31 días
            return 31

    # Calculo para el eje de las x en la grafica datos diarios
    def ejeX(self, mes=None, tiempo_db = None):
        if mes is None:
            mes = date.today().month
        horario = list()
        # estas variables es para indentificar los meses que llevan estos horarios basados en horas
        horario_7_17 = [1,2,10,11,12]
        horario_7_18 = [3]
        horario_6_18 = [4,5,6,7,8]
        horario_6_17 = [9]

        # Estas condiciones son para listar los horarios por el mes
        if int(mes) in horario_7_17:
            for m in list(range(7,18)):
                horario.append(str(m))
        elif int(mes) in horario_7_18:
            for m in list(range(7,19)):
                horario.append(str(m))
        elif int(mes) in horario_6_18:
            for m in list(range(6,19)):
                horario.append(str(m))
        elif int(mes) in horario_6_17:
            for m in list(range(6,18)):
                horario.append(str(m))
        else:
            return 'Ha Ocurrido un error en el mes'

        # Este bucle es para agregar los minutos a ejex grafico
        # for i in tiempo_db:
        #     index = tiempo_db.index(i)
        #     horario[index] = i
        return horario

    # Esta funcion para cargar datospara el grafico diario
    def graficos(self, est, fech):
        estaciones = {'D':355, 'J':330, 'F':321, 'T':342}
        estacion = estaciones[est]
        str_to_fecha = datetime.strptime(fech, '%Y-%m-%d')
        fecha = str_to_fecha.strftime('%Y-%m-%d')
        qry = SeocModel.objects.filter(estacion = estacion, fecha = fecha).values('tiempo','eoa', 'eoan','estacion')
        tiempo_db = []
        eoa = []
        eoan = []
        for m in qry:
            tiempo_db.append(m['tiempo'].strftime('%H:%M'))
            if m['eoa'] == -999: 
                eoa.append(None)
            else:
                a = m['eoa']
                formato = '{:9.4f}'.format(a)
                eoa.append(float(formato))
            if m['eoan'] == -999:
                eoan.append(None)
            else:
                an = m['eoan']
                formato = '{:9.4f}'.format(an)
                eoan.append(float(formato))
        
        ejex_base = self.ejeX(str_to_fecha.month, tiempo_db)
        contar_ejex = len(ejex_base)
        contar_eoa = len(eoa)
        contar_eoan = len(eoan)
        restar_eoa = contar_ejex - contar_eoa
        for m in list(range(0,restar_eoa)):
            eoa.append(None)
        
        restar_eoan = contar_ejex - contar_eoan
        for n in list(range(0,restar_eoan)):
            eoan.append(None)
        from core.servicios.actino.models import ActinoEstacionesModel

        msg = "No se presentaron las condiciones para el cálculo"        
        for t in eoa:
            if type(t) == float:
                msg = ''
        for t in eoan:
            if type(t) == float:
                msg = ''
        
        data = {'tiempo': ejex_base, 'eoa': eoa, 'eoan':eoan, 'mensaje': msg}
        return data

    def fechaUTC(self,fecha, tiempo):
        str_fecha = fecha+" "+tiempo
        str_format = "%Y-%m-%d %H:%M:%S"
        strTodatetime = datetime.strptime(str_fecha, str_format)
        total_milisegundos = (strTodatetime - datetime(1970,1,1)).total_seconds() * 1000
        return total_milisegundos

    def graficos_mensual(self, est, year, month):
        estaciones = {'D':355, 'J':330, 'F':321, 'T':342}
        estacion = estaciones[est]
        data = dict()
        list_eoa = list()  # lista donde se almacena tiempo UTC y eoa
        list_eoan = list() # lista donde se almacena tiempo UTC y eoan
        for i in self.model.objects.filter(estacion = estacion, fecha__year= year, fecha__month = month):
            fechaUTC = self.fechaUTC(str(i.fecha), str(i.tiempo)) # Comvertir formato de fecha y hora base datos en UTC
            # Estas condiciones es para convertir los datos del eoa y eoan
            if i.eoa < 0:
                eoa = None
            else:
                formato = '{:9.4f}'.format(i.eoa)
                eoa = float(formato)
            
            if i.eoan < 0:
                eoan = None
            else:
                formato = '{:9.4f}'.format(i.eoan)
                eoan = float(formato)
            # Se agrega a la lista los datos con su tiempo correspondente en UTC
            list_eoa.append([fechaUTC,eoa])
            list_eoan.append([fechaUTC,eoan])
        data['eoa'] = list_eoa
        data['eoan'] = list_eoan
        # Para verificar si el mes a presentado las codicones para el calculo
        msg = "En el mes no se han presentado condiciones para el cálculo"
        for t in list_eoa:
            if type(t[1]) == float:
                msg = ''
        for t in list_eoan:
            if type(t[1]) == float:
                msg = ''
        data['mensaje'] = msg

        # calcular minimo y maximo del ejex del a grafica
        fecha_min_max = dict()
        dias_mes = self.obtener_dias_del_mes(month, year)
        fecha_min_str = f'{year}-{month}-1'
        fecha_max_str = f'{year}-{month}-{dias_mes}'
        fecha_min_max['min'] = self.fechaUTC(fecha_min_str, '00:00:00')
        fecha_min_max['max'] = self.fechaUTC(fecha_max_str, '23:59:00')
        data['min_max'] = fecha_min_max

        return data

    def post(self, request, *args , **kwargs):
        data = {}
        try:
            accion = request.POST.get('accion')
            # Esta condicion es para los datos de garficos diarios
            if accion == 'datos_graficos':
                fecha_dia = request.POST.get('fecha')
                data['cmw'] = self.graficos('D',fecha_dia)
                data['jvn'] = self.graficos('J',fecha_dia)
                data['tcp'] = self.graficos('T',fecha_dia)
                data['lfe'] = self.graficos('F',fecha_dia)
            # Condicion para el mes actual. Es el que muestra al cargar la pagina
            elif accion == 'datos_graficos_mes':
                fecha_m = request.POST.get('fecha_m')
                fecha = datetime.strptime(fecha_m, '%Y-%m-%d')
                data['cmwM'] = self.graficos_mensual('D', fecha.year, fecha.month)
                data['jvnM'] = self.graficos_mensual('J', fecha.year, fecha.month)
                data['tpcM'] = self.graficos_mensual('T', fecha.year, fecha.month)
                data['lfeM'] = self.graficos_mensual('F', fecha.year, fecha.month)
            # Condicion para la busqueda del grafico mensual
            elif accion == 'buscar_gmes':
                month = request.POST.get('mes')
                year = request.POST.get('anio')
                data['cmwM'] = self.graficos_mensual('D', year, month)
                data['jvnM'] = self.graficos_mensual('J', year, month)
                data['tpcM'] = self.graficos_mensual('T', year, month)
                data['lfeM'] = self.graficos_mensual('F', year, month)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data = data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Servicios SEOC'
        context['titulo_page'] = 'Servicio de Espesor Óptico para Cuba'
        context['modelo'] = WebModelo.objects.last()
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')
        
        return context

# Estacion Automatica
class MetView(TemplateView):
    template_name = 'web/servicios/met/index_met.html'
    model = MetModel

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        try:
            servicios_estado = leer_estado_servicios()
            if servicios_estado['met'] is False:
                return redirect('servicio_interrupto')
        except FileNotFoundError:
            escribir_estado_servicios({'actino': False, 'met': False, 'seoc': False, 'pyra_par': False})
            return redirect('servicio_interrupto')
        return super().dispatch(request, *args, **kwargs)

    # Datos Historicos
    def get_historicos(self):
        dicc = dict()
        dicc['vv'] = MetHistoricosModel.objects.get(variable='vv')
        dicc['ri'] = MetHistoricosModel.objects.get(variable='ri')
        dicc['hi'] = MetHistoricosModel.objects.get(variable='hi')

        dicc['hr_max'] = MetHistoricosModel.objects.filter(variable='hr', tipo='MAX').last()
        dicc['hr_min'] = MetHistoricosModel.objects.filter(variable='hr', tipo='MIN').last()
        dicc['ta_max'] = MetHistoricosModel.objects.filter(variable='ta', tipo='MAX').last()
        dicc['ta_min'] = MetHistoricosModel.objects.filter(variable='ta', tipo='MIN').last()
        dicc['pr_max'] = MetHistoricosModel.objects.filter(variable='pr', tipo='MAX').last()
        dicc['pr_min'] = MetHistoricosModel.objects.filter(variable='pr', tipo='MIN').last()
        return dicc

    # Convertir fecha datetime UTC milisegundos
    def fechaUTC(self,fecha):
        total_milisegundos = (fecha - datetime(1970,1,1)).total_seconds() * 1000
        return total_milisegundos

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            accion = request.POST.get('accion')
            fecha = request.POST.get('fecha')
            if accion == 'get_data':
                qry = self.model.objects.latest('fecha').toJSON() # Consulta del ultimo registro
                data['gauge'] = qry # Aqui van los datos que no son acumulados 48 horas
                last_fecha = datetime.strptime(qry['datetime'], '%Y-%m-%d %H:%M:%S') # Fecha del ultimo registro
                restar_dos_dia = last_fecha - timedelta(2) # Restar dos dias fecha del resgistro
                # Acumulado 48 horas antes de RC
                qry_acumulado = self.model.objects.filter(fecha__range=(restar_dos_dia,last_fecha)).aggregate(Sum('rc'))
                # Comportamiento en las ultimos 48 horas
                qry_comp48 = self.model.objects.filter(fecha__range=(restar_dos_dia,last_fecha)).order_by('fecha')
                rc = list()
                ta = list()
                pr = list()
                hr = list()
                vv = list()
                dv = list()
                for m in qry_comp48:
                    fecha_milisegundo = self.fechaUTC(m.fecha) # convierte la fecha en milisegundo por asi los soporta highcharts
                    rc.append([fecha_milisegundo,m.rc])
                    ta.append([fecha_milisegundo,m.ta])
                    pr.append([fecha_milisegundo,m.pr])
                    hr.append([fecha_milisegundo,m.hr])
                    vv.append([fecha_milisegundo,m.vv])
                    dv.append([fecha_milisegundo,m.dv])
                data['mm_acomulado'] = qry_acumulado
                data['acomulado48'] = {'rc':rc,'ta': ta, 'pr':pr, 'hr':hr, 'vv':vv,'dv': dv}
                fecha_inicio = self.fechaUTC(last_fecha)
                fecha_dos_dias = self.fechaUTC(restar_dos_dia)
                data['fecha_inicial_final'] = {"fecha_inicio": fecha_dos_dias, 'fecha_final': fecha_inicio}
            elif accion == 'buscar_fecha':
                qry = MetModel.objects.filter(fecha__date = fecha).last()
                if qry is None:
                    data['error'] = 'No existen datos con esta fecha'
                else:
                    tojson = qry.toJSON()
                    data['gauge'] = tojson
                    last_fecha = datetime.strptime(tojson['datetime'], '%Y-%m-%d %H:%M:%S') # Fecha del ultimo registro
                    restar_dos_dia = last_fecha - timedelta(2) # Restar dos dias fecha del resgistro
                    # Acumulado 48 horas antes de RC
                    qry_acumulado = self.model.objects.filter(fecha__range=(restar_dos_dia,last_fecha)).aggregate(Sum('rc'))
                    # Comportamiento en las ultimos 48 horas
                    qry_comp48 = self.model.objects.filter(fecha__range=(restar_dos_dia,last_fecha)).order_by('fecha')
                    rc = list()
                    ta = list()
                    pr = list()
                    hr = list()
                    vv = list()
                    dv = list()
                    for m in qry_comp48:
                        fecha_milisegundo = self.fechaUTC(m.fecha) # convierte la fecha en milisegundo por asi los soporta highcharts
                        rc.append([fecha_milisegundo,m.rc])
                        ta.append([fecha_milisegundo,m.ta])
                        pr.append([fecha_milisegundo,m.pr])
                        hr.append([fecha_milisegundo,m.hr])
                        vv.append([fecha_milisegundo,m.vv])
                        dv.append([fecha_milisegundo,m.dv])
                    data['mm_acomulado'] = qry_acumulado
                    data['acomulado48'] = {'rc':rc,'ta': ta, 'pr':pr, 'hr':hr, 'vv':vv,'dv': dv}
                    fecha_inicio = self.fechaUTC(last_fecha)
                    fecha_dos_dias = self.fechaUTC(restar_dos_dia)
                    data['fecha_inicial_final'] = {"fecha_inicio": fecha_dos_dias, 'fecha_final': fecha_inicio}
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data = data, safe=False)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Servicios Estación Automática'
        context['titulo_page'] = 'Estación Automática Vaisala WTX-520'
        context['modelo'] = WebModelo.objects.last()
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        context['historicos'] = MetHistoricosModel.objects.all()
        context['card_historicos'] = self.get_historicos()

        return context

# Pyra & Par
class PyraParView(TemplateView):
    template_name = 'web/servicios/pyra_par/pyra_par_index.html'
    model = Pyra_ParModel

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        try:
            servicios_estado = leer_estado_servicios()
            if servicios_estado['pyra_par'] is False:
                return redirect('servicio_interrupto')
        except FileNotFoundError:
            escribir_estado_servicios({'actino': False, 'met': False, 'seoc': False, 'pyra_par': False})
            return redirect('servicio_interrupto')
        return super().dispatch(request, *args, **kwargs)

    def fechaUTC(self,fecha):
        total_milisegundos = (fecha - datetime(1970,1,1)).total_seconds() * 1000
        return total_milisegundos

    def fechaX(self,fecha):
        total_milisegundos = (fecha - datetime(1970,1,1) + timedelta(hours=5)).total_seconds() * 1000
        return total_milisegundos

    def get_data_salida_puesta(self,fecha):
        # act_model = ActinoEstacionesModel.objects.get(codigo=355)
        data = salida_puesta(fecha)

        salida_ = self.fechaX(data["salida"])
        puesta_ = self.fechaX(data["puesta"])

        return {"salida":salida_, "puesta":puesta_}

    def post(self, request, *args, **kwargs):
        data = {}

        try:
            accion = request.POST.get('accion')
            fecha = request.POST.get('fecha')
            sal_puest = self.get_data_salida_puesta(fecha)

            if accion == 'get_data':
                pyra  = list()
                par = list()
                qry = self.model.objects.filter(fecha__date = fecha).order_by('fecha')
                if qry:
                    for m in qry:
                        fecha_milisegundo = self.fechaUTC(m.fecha)
                        calc_pyra = m.pyra / (m.factor_pyra / 1000)
                        calc_par = m.par * m.factor_par
                        pyra.append([fecha_milisegundo,calc_pyra])
                        par.append([fecha_milisegundo,calc_par])
                    data['pyra'] = pyra
                    data['par'] = par
                    # format_ = '%Y-%m-%d %H:%M:%S'
                    # str_fecha_inicio = f'{fecha} 00:00:00'
                    # str_fecha_final = f'{fecha} 23:59:00'
                    # fecha_inicio = datetime.strptime(str_fecha_inicio, format_)
                    # fecha_final = datetime.strptime(str_fecha_final, format_)
                    data['fecha_inicio_final'] = sal_puest
                    data['mensaje'] = ''
                    data['fecha'] = fecha

                else:
                    data['pyra'] = 0
                    data['par'] = 0
                    data['fecha_inicio_final'] = sal_puest

                    data['mensaje'] = 'No hay datos en esta fecha'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data = data, safe=False)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Estación Automática Radiación Solar'
        context['titulo_page'] = 'Estación Automática Radiación Solar'
        context['modelo'] = WebModelo.objects.last()
        context['noticias'] = NoticiasModels.objects.filter(estado=True).values('id')
        context['nav_inv'] = CatInvestigacionesModel.objects.all()
        # context['pyra_max'] = self.model.objects.aggregate(Max('pyra'))['pyra__max']
        # context['par_max'] = self.model.objects.aggregate(Max('par'))['par__max']

        return context

# Pagina Servicio Error
class ServicioInterruptoTemplateView(TemplateView):
    template_name = 'web/servicio_interrupto.html'
