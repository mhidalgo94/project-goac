import os
from datetime import datetime
from django.utils import timezone
from django.views.generic import UpdateView
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy

from config.settings import LOG_ERROR_SEOC
from core.servicios.seoc.models import SeocModel, SeocAPIToken
from core.log_error import estado_log

from core.servicios.seoc.forms import SeocAPIKeyForms, SeocForm
from core.servicios.seoc.models import SeocModel
from core.servicios.actino.models import ActinoEstacionesModel

class SeocDatosListView(LoginRequiredMixin,ListView):
    model = SeocModel
    template_name = 'panel/servicios/seoc/datos_seoc.html'

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
                estacion = request.POST['estacion']
                qry = self.model.objects.filter(estacion=estacion,fecha__range=[f_inicial, f_final])
                for i in qry:
                    data.append(i.toJSON())
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Lista de Datos SEOC'
        context['info'] = {'head_card': 'Lista de Datos SEOC', 'icono': 'fas fa-table' }
        context['codig_esta'] = ActinoEstacionesModel.objects.all()
        return context


class SeocUpdateView(LoginRequiredMixin, UpdateView):
    model = SeocModel
    form_class = SeocForm
    template_name = 'panel/servicios/seoc/edit_datos_seoc.html'
    success_url = reverse_lazy('list_seoc')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Editar SEOC"
        context['info'] = {'head_card': 'Editar Datos SEOC', 'icono': 'fas fa-edit'}
        return context

class SeocAPITokenList(LoginRequiredMixin,ListView):
    model = SeocAPIToken
    template_name = 'panel/servicios/seoc/token.html'
    form_class = SeocAPIKeyForms

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
        context['titulo'] = 'GOAC | Editar Key SEOC'
        context['info'] = {'head_card': 'Editar Token SEOC', 'icono': 'fas fa-edit' }
        context['form'] = self.form_class()
        return context


# class SeocErrorView(LoginRequiredMixin, TemplateView):
#     template_name = 'panel/servicios/seoc/error.html'

#     @csrf_exempt
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_superuser is False:
#             messages.error(request, 'No tienes permisos suficiente para acceder')
#             return redirect('panel')
#         return super().dispatch(request, *args, **kwargs)


#     def post(self,request, *args,**kwargs):
#         data = {}
#         try:
#             accion = request.POST.get('accion')
#             if accion == 'delete_log':
#                 if os.path.exists(LOG_ERROR_SEOC):
#                     os.remove(LOG_ERROR_SEOC)
#         except:
#             data['error'] = 'No se pudo eliminar el archivo'
#         return JsonResponse(data)

#     def read_log_error(self):
#         try:
#             with open(LOG_ERROR_SEOC, 'r') as doc:
#                 read = doc.readlines()
#             return read
#         except:
#             return False

#     def lectura_log(self):
#         lectura = self.read_log_error()
#         if lectura is True:
#             return lectura[::-1]
#         else:
#             return 'El archivo de registro no existe'

#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         context['titulo'] = "GOAC | Servicos Actino | Errores"
#         context['info'] = {'head_card': 'Log de Errores SEOC', 'icono': 'fas fa-exclamation-triangle' }
#         context['log'] = estado_log(LOG_ERROR_SEOC)
#         return context
