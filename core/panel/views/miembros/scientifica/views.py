from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView
from django.views.decorators.csrf import csrf_exempt

from core.miembros.models import SCientificaModel
from core.miembros.forms import SCientificaForm


# Sociedades Cientifas relacionadas con los miembros del Grupo
class SCientificasListView(LoginRequiredMixin,ListView):
    model = SCientificaModel
    template_name = 'panel/miembros/scientifica/list_scientifica.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
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
            elif action== 'eliminar':
                id_ = request.POST['id']
                m = self.model.objects.get(id=id_)
                m.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Sociedades Científicas'
        context['info'] = {'local': 'Datos de Sociedades Científicas', 'head_card': 'Sociedades Científicas', 'icono': 'fas fa-atom' }
        return context


class SCientificaCreateView(LoginRequiredMixin,CreateView):
    model = SCientificaModel
    form_class = SCientificaForm
    template_name = 'panel/miembros/scientifica/create_scientifica.html'
    success_url = reverse_lazy('list_scientifica')


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Crear Instrumento'
        context['info'] = {'local': 'Crear Sociedad Científica', 'head_card': 'Crear Sociedad Científica', 'icono': 'fas fa-plus' }
        return context

class SCientificaUpdateView(LoginRequiredMixin,UpdateView):
    model = SCientificaModel
    form_class = SCientificaForm
    template_name = 'panel/miembros/scientifica/edit_scientifica.html'
    success_url = reverse_lazy('list_scientifica')


    def dispatch(self,request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        self.object = self.get_object()
        return super().dispatch(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Actualizar Sociedad Científica'
        context['info'] = { 'head_card': 'Actualizar Sociedad Científica', 'icono': 'fas fa-edit' }
        return context  

