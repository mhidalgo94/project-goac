from datetime import datetime
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from core.servicios.pyra_par.models import Pyra_ParModel, PyParAPIToken
from core.servicios.pyra_par.froms import APITokenForm

class PyraParDatosListView(LoginRequiredMixin,ListView):
    model = Pyra_ParModel
    template_name = 'panel/servicios/pyra_par/datos/datos_pyra_par.html'

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
        context['titulo'] = 'GOAC | Lista de Datos Pyra Par'
        context['info'] = {'head_card': 'Lista de Datos Pyra y Par', 'icono': 'fas fa-table' }

        return context


class PyParAPITokenListView(LoginRequiredMixin,ListView):
    model = PyParAPIToken
    template_name = 'panel/servicios/pyra_par/datos/token.html'
    form_class = APITokenForm

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
        context['titulo'] = 'GOAC | Editar Key Pyra Par'
        context['info'] = {'head_card': 'Editar Token Pyra y Par', 'icono': 'fas fa-edit' }
        context['form'] = self.form_class()
        return context

