import os
from datetime import datetime
from django.utils import timezone
from django.views.generic import UpdateView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy

from config.settings import LOG_ERROR_SEOC
from core.servicios.seoc.models import SeocModel, SeocAPIToken
from core.log_error import estado_log

from core.servicios.met.forms import MetForm, MetAPIKeyForms, MetHistoricosForm
from core.servicios.met.models import MetHistoricosModel, MetModel, MetAPITokenModel

class MetDatosListView(LoginRequiredMixin,ListView):
    model = MetModel
    template_name = 'panel/servicios/met/datos_met.html'

    # @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder a usuarios')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def to_datetime(self,dtime):
        format_ = "%d-%m-%Y %H:%M"
        to_datetime = datetime.strptime(str(dtime),format_)
        return to_datetime

    def post(self, request,*args,**kwargs):
        data={}
        try:
            action = request.POST['accion']
            if action=='buscar_archivos':
                data=[]
                for i in self.model.objects.filter(fecha__range=[timezone.now().replace(hour=0, minute=0, second=0), timezone.now().replace(hour=23, minute=59, second=59)]):
                    data.append(i.toJSON())
            elif action== 'eliminar':
                id_ = request.POST['id']
                m = self.model.objects.get(id=id_)
                m.delete()
            elif action == "filter":
                data = []
                f_inicial = self.to_datetime(request.POST['fechaInicial'])
                f_final = self.to_datetime(request.POST['fechaFinal'])
                qry = self.model.objects.filter(fecha__range=[f_inicial, f_final])
                for i in qry:
                    data.append(i.toJSON())
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Lista de Datos Estación Automática'
        context['info'] = {'head_card': 'Lista de Datos Estación Automática', 'icono': 'fas fa-table' }
        return context

class MetUpdateView(LoginRequiredMixin, UpdateView):
    model = MetModel
    form_class = MetForm
    template_name = 'panel/servicios/met/edit_datos_met.html'
    success_url = reverse_lazy('list_met')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Editar Estación Automática"
        context['info'] = {'head_card': 'Editar Datos Estación Automática', 'icono': 'fas fa-edit'}
        return context


class MetAPITokenList(LoginRequiredMixin,ListView):
    model = MetAPITokenModel
    template_name = 'panel/servicios/met/token.html'
    form_class = MetAPIKeyForms

    # @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder a usuarios')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request,*args,**kwargs):
        data={}
        try:
            action = request.POST['action']
            if action=='searchdata':
                data=[]
                for i in self.model.objects.all():
                    data.append(i.toJSON())
            elif action == 'update':
                id_ = request.POST['id']
                m = self.model.objects.get(id=id_)
                m.save()
            elif action== 'eliminar':
                id_ = request.POST['id']
                m = self.model.objects.get(id=id_)
                m.delete()
            elif action == 'add-apikey':
                form =self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                else:
                    data['error']= form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Editar APIKey Estación Automática'
        context['info'] = {'head_card': 'Editar API Token Estación Automática', 'icono': 'fas fa-edit' }
        context['form'] = self.form_class()
        return context


class MetErrorView(LoginRequiredMixin, TemplateView):
    template_name = 'panel/servicios/met/error.html'

    @csrf_exempt
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
                if os.path.exists(LOG_ERROR_SEOC):
                    os.remove(LOG_ERROR_SEOC)
        except:
            data['error'] = 'No se pudo eliminar el archivo'
        return JsonResponse(data)

    def read_log_error(self):
        try:
            with open(LOG_ERROR_SEOC, 'r') as doc:
                read = doc.readlines()
            return read
        except:
            return False

    def lectura_log(self):
        lectura = self.read_log_error()
        if lectura is True:
            return lectura[::-1]
        else:
            return 'El archivo de registro no existe'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Servicos Estación Automática | Errores"
        context['info'] = {'head_card': 'Log de Errores Estación Automática', 'icono': 'fas fa-exclamation-triangle' }
        context['log'] = estado_log(LOG_ERROR_SEOC)
        return context


# Lista Historicos
class MetHistoricosListView(LoginRequiredMixin,ListView):
    model = MetHistoricosModel
    form_class = MetHistoricosForm
    template_name = 'panel/servicios/met/historicos.html'

    # @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder a usuarios')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request,*args,**kwargs):
        data={}
        try:
            action = request.POST['accion']
            if action=='buscar_archivos':
                data=[]
                for i in self.model.objects.all():
                    data.append(i.toJSON())
            elif action== 'eliminar':
                id_ = request.POST['id']
                m = self.model.objects.get(id=id_)
                m.delete()
            elif action == 'agregar-historicos':
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Lista de Históricos Estación Automática'
        context['info'] = {'head_card': 'Lista de Históricos Estación Automática', 'icono': 'fas fa-table' }
        context['form'] = MetHistoricosForm()
        return context


# Actualizar historicos
class MetHistoricosUpdateView(LoginRequiredMixin, UpdateView):
    model = MetHistoricosModel
    form_class = MetHistoricosForm
    template_name = 'panel/servicios/met/edit_historicos.html'
    success_url = reverse_lazy('list_met_historicos')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Editar Históricos Estación Automática"
        context['info'] = {'head_card': 'Editar Históricos Estación Automática', 'icono': 'fas fa-edit'}
        return context
