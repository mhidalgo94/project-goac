import os
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.edit import CreateView

from config.settings import ACTINO_ROOT, ACTINO_HISTORICOS_ROOT, LOG_ERROR_ACTINO,LOG_ERROR_ACTINO
from core.servicios.actino.models import ActinoHorarioVeranoModel, ActinoObservadorModel, ActinoEstacionesModel
from core.servicios.actino.forms import ActinoHorarioVeranoForm, ObservadorForms, EstacionesForm
from core.log_error import read_log_error, save_log, estado_log


# Lista de observadores
class ObservadoresListView(LoginRequiredMixin, ListView):
    model = ActinoObservadorModel
    template_name = 'panel/servicios/actino/observadores/list_observadores.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwarg):
        try:
            action = request.POST['action']
            if action == 'delete':
                obv = ActinoObservadorModel.objects.get(id=request.POST['id'])
                obv.delete()
                return redirect(reverse_lazy('list_observadores'))
            elif action == 'edit':
                obv = ActinoObservadorModel.objects.get(id=request.POST['id'])
                obv.nombre = request.POST['nombre']
                if len(request.FILES) == 0:
                    obv.imagen = ""
                else:
                    obv.imagen = request.FILES['imagen']
                obv.estacion = request.POST['estacion']
                obv.save()
            elif action == 'add-observador':
                form = ObservadorForms(files=request.FILES, data=request.POST)
                if form.is_valid():
                    form.save()
                    return redirect(reverse_lazy('list_observadores'))
                else:
                    messages.error(request, 'Al parecer tiene el mismo codigo')
                    return redirect(reverse_lazy('list_observadores'))
            else:
                messages.error(request, 'Al parecer tiene el mismo codigo')
                return redirect(reverse_lazy('list_observadores'))
        except Exception as e:
            save_log(LOG_ERROR_ACTINO,str(e))
            messages.error(request, str(e))
        return redirect(reverse_lazy('list_observadores'))

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Servicios Actinométrico"
        context['info'] = {'head_card': 'Lista de Observadores', 'icono': 'fas fa-glasses' }
        context['form'] = ObservadorForms()
        context['obv'] = ActinoObservadorModel.objects.all()
        return context

# Control de archivos 
class ArchivosActinoView(LoginRequiredMixin, TemplateView):
    template_name = 'panel/servicios/actino/archivos/archivos_actino.html'

    # @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    # Inicia con los detalles de la carpeta al iniciar la pagina    
    def detalles_carpeta(self):
        # Todos los archivos
        all_files = os.listdir(ACTINO_ROOT)
        # Cantidad de archivos
        cant_archivos = 0
        # Fecha de modificacion
        folder_modif = os.path.getmtime(ACTINO_ROOT)
        date_modif = datetime.fromtimestamp(folder_modif)
        # Tamano de todos los archivos
        archivo_size = list()
        carpeta_size = 0  
        for archivo in all_files:
            cant_archivos = cant_archivos + 1
            path_archivo = os.path.join(ACTINO_ROOT, archivo)
            # Sumar tamano de todos los archivos
            if not os.path.islink(archivo):
                carpeta_size += os.path.getsize(path_archivo)
                archivo_size.append(os.path.getsize(path_archivo))
        files_ = {'cant_arch': cant_archivos,'carpeta_size': carpeta_size, 'modific': date_modif}

        return files_
    
    # Retorna informacion los archivos con su tamano solo ingresar
    # el path de la carpeta
    def info_archivos(self,path):
        all_files = os.listdir(path)
        archivo_size = list()
        datos = list()
        for archivo in all_files:
            path_archivo = os.path.join(path, archivo)
            # Sumar tamano de todos los archivos
            if not os.path.islink(archivo):
                archivo_size= '{:.3}{}'.format(os.path.getsize(path_archivo)/float(1<<10)," KB")
                archivo_mas_tamano = {'archivo': archivo, 'tamano': archivo_size}
                datos.append(archivo_mas_tamano)
        return datos

    # Subir archivos de actino tanto los diario como los historicos solo
    # solo hay ingresar el archivo y el path
    def subir_archivo(self, archivo, path):
        nombre_archivo = str(archivo)
        directorio = str(path+"/")
        if os.path.exists(path):
            with open(directorio + nombre_archivo, 'wb') as arch:
                for chunk in archivo.chunks():
                    arch.write(chunk)
                    return f'Archivo "{nombre_archivo}" guardado correctamente'
        
    # Para eliminar el archivo
    def eliminar_file(self, path ,file_name, usuario=None):
        path_archivo = os.path.join(path, file_name)
        if os.path.exists(path_archivo):
            os.remove(path_archivo)
            msg = 'Archivo '+file_name+' eliminado correctamente por: '+usuario
            save_log(LOG_ERROR_ACTINO,msg)
            return msg
        else:
            msg = 'No existe este archivo'+file_name
            save_log(LOG_ERROR_ACTINO,msg)
        
        return False

    # Lee el archivo para el funcionamiento btn lectura file
    def leer_archivo(self,archivo):
        path = os.path.join(ACTINO_ROOT,archivo)
        with open(path,'r') as f:
            lectura = f.read()
            return lectura
    # Peticiones Post
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            accion = request.POST.get('accion')
            archivo = request.POST.get('archivo')
            usuario = request.user.username
            if accion == 'buscar_archivos':
                data['datos'] = self.info_archivos(ACTINO_ROOT)

            elif accion == 'eliminar':
                especificar_carpeta = request.POST.get('path')
                carpeta_root = ACTINO_ROOT
                if especificar_carpeta == 'historico':
                    carpeta_root = ACTINO_HISTORICOS_ROOT
                    info = self.eliminar_file(carpeta_root,archivo, usuario)
                    data = info
                else:
                    info = self.eliminar_file(carpeta_root,archivo, usuario)
                    data = info
            elif accion == 'subir-archivo':
                archivo = self.request.FILES['file']
                if '.csv' in str(archivo):
                    respuesta = self.subir_archivo(self.request.FILES['file'], ACTINO_ROOT)
                    data = respuesta
                else:
                    data['error'] = 'No es un archivo csv'
            elif accion == 'buscar_archivos_historicos':
                data['datos_historicos'] = self.info_archivos(ACTINO_HISTORICOS_ROOT)
            elif accion == 'subir-archivo-historico':
                respuesta = self.subir_archivo(self.request.FILES['file'],ACTINO_HISTORICOS_ROOT)
                data = respuesta
            elif accion == 'leer-archivo':
                lectura = self.leer_archivo(archivo)
                data['lectura'] = lectura
            else:
                data['error'] = 'Ha ocurrido un error'

        except Exception as e:
            save_log(LOG_ERROR_ACTINO,str(e))
            data['error'] = str(e)

        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Servicos Actino | Archivos"
        context['info'] = {'head_card': 'Archivos de Actino', 'icono': 'fas fa-file-alt' }
        context['carpeta_detalles'] = self.detalles_carpeta()
        return context

# Control de Errores
class ActinoErrorView(LoginRequiredMixin, TemplateView):
    template_name = 'panel/servicios/actino/log/error.html'

    # @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)


    def post(self,request, *args,**kwargs):
        data = {}
        try:
            accion = request.POST.get('accion')
            if accion == 'delete_log':
                path_archivo = LOG_ERROR_ACTINO
                if os.path.exists(path_archivo):
                    os.remove(path_archivo)
        except:
            data['error'] = 'No se pudo eliminar el archivo'
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Servicos Actino | Errores"
        context['info'] = {'head_card': 'Log de Errores Actino', 'icono': 'fas fa-exclamation-triangle' }
        context['log'] = estado_log(LOG_ERROR_ACTINO)
        return context


# Control de Estaciones y Horario de verano
class ActinoControlEstacionesView(LoginRequiredMixin, ListView):
    model = ActinoEstacionesModel
    template_name = 'panel/servicios/actino/estaciones/estaciones.html'

    # @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            accion = request.POST.get('accion')
            codigo_ = request.POST.get('codigo')
            estado_verano = ActinoHorarioVeranoModel.objects.last()

            if accion == 'eliminar':
                estacion = ActinoEstacionesModel.objects.get(codigo=codigo_)
                estacion.delete()
            elif accion == 'act_verano':
                form = ActinoHorarioVeranoForm(request.POST,instance=estado_verano)
                if form.is_valid():
                    form.save()
                    return redirect(reverse_lazy('control_estaciones'))
                
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        estado_verano = ActinoHorarioVeranoModel.objects.last()
        context['titulo'] = "GOAC | Estaciones Actino"
        context['info'] = {'head_card': 'Estaciones Actino', 'icono': 'fas fa-map-marker-alt' }
        context['horario_verano'] = timezone.now()
        context['est_activas'] = self.model.objects.filter(estado__nombre="ACTIVO")
        context['est_noactivas'] = self.model.objects.all().exclude(estado__nombre="ACTIVO")
        context['form'] = ActinoHorarioVeranoForm(instance=estado_verano)
        return context


class ActinoEstacionUpdateView(LoginRequiredMixin, UpdateView):
    model = ActinoEstacionesModel
    form_class = EstacionesForm
    template_name = 'panel/servicios/actino/estaciones/edit_estacion.html'
    success_url = reverse_lazy('control_estaciones')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self,):
        codigo_ = self.kwargs.get('codigo')
        return get_object_or_404(self.model, codigo=codigo_)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Editar Estacióm Actino"
        context['info'] = {'head_card': 'Editar Estacion Actino', 'icono': 'fas fa-edit'}
        return context


class ActinoEstacionCreateView(LoginRequiredMixin, CreateView):
    model = ActinoEstacionesModel
    form_class = EstacionesForm
    template_name = 'panel/servicios/actino/estaciones/create_estacion.html'
    success_url = reverse_lazy('control_estaciones')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Nueva Estación Actino"
        context['info'] = {'head_card': 'Crear nueva Estación Actino', 'icono': 'fas fa-plus'}
        return context

