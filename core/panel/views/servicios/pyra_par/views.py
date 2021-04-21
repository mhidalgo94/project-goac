from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, UpdateView, CreateView, FormView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from core.servicios.pyra_par.models import Pyra_ParModel, APIToken

class PyraParDatosListView(LoginRequiredMixin,ListView):
    model = Pyra_ParModel
    template_name = 'panel/servicios/pyra_par/datos/datos_pyra_par.html'

    @csrf_exempt
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
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Lista de Datos Pyra Par'
        context['info'] = {'head_card': 'Lista de Datos Pyra y Par', 'icono': 'fas fa-table' }
        return context


class APITokenFormView(LoginRequiredMixin,ListView):
    model = APIToken
    template_name = 'panel/servicios/pyra_par/datos/token.html'

    @csrf_exempt
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
                print(data)
            elif action== 'eliminar':
                id_ = request.POST['id']
                m = self.model.objects.get(id=id_)
                m.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Editar Key Pyra Par'
        context['info'] = {'head_card': 'Editar Token Pyra y Par', 'icono': 'fas fa-edit' }
        return context

