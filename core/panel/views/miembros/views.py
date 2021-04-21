from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,  UpdateView, CreateView
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.views.generic.edit import FormView


from core.miembros.models import MiembrosModel, SCientificaModel
from core.miembros.forms import  MiembrosForm, SCientificaForm


# Miembros del Grupo
class MiembrosListView(LoginRequiredMixin,ListView):
    model = MiembrosModel
    template_name = 'panel/miembros/list_miembros.html'

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
        context['titulo'] = 'GOAC | Lista de Miembros'
        context['info'] = {'local': 'Datos de Miembros', 'head_card': 'Miembros', 'icono': 'fas fa-user-friends' }
        return context

class MiembrosCreateView(LoginRequiredMixin,CreateView):
    model = MiembrosModel
    model_modal = SCientificaModel
    form_class = MiembrosForm
    form_modal = SCientificaForm
    template_name = 'panel/miembros/create_miembros.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add-scientifica':
                modal = self.model_modal()
                modal.nombre = request.POST['nombre']
                modal.url = request.POST['url']
                modal.desc = request.POST['desc']
                modal.save()
            elif action == 'create-miembro':
                form = self.form_class(data = request.POST, files= request.FILES) 
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Agregar Miembros'
        context['info'] = {'local': 'Panel Administracion', 'head_card': 'Agregar Miembros' , 'icono': 'fas fa-plus mr-2'}
        context['modal'] = self.form_modal()
        return context

class MiembrosUpdateView(LoginRequiredMixin,UpdateView):
    model = MiembrosModel
    model_modal = SCientificaModel
    form_class = MiembrosForm
    form_modal = SCientificaForm
    template_name = 'panel/miembros/edit_miembros.html'
    success_url = reverse_lazy('list_miembros')

    def dispatch(self,request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        self.object = self.get_object()
        return super().dispatch(request,*args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add-scientifica':
                modal = self.model_modal()
                modal.nombre = request.POST['nombre']
                modal.url = request.POST['url']
                modal.desc = request.POST['desc']
                modal.save()
            elif action == 'edit-miembro':
                _instance = self.get_object()
                form = self.form_class(data = request.POST,instance=_instance,files= request.FILES)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Editar Miembro'
        context['info'] = {'local': 'Panel Miembros', 'head_card': 'Actualizar Miembro', 'icono': 'fas fa-edit' }
        context['modal'] = self.form_modal()
        return context    

class PefilMiembroEditView(LoginRequiredMixin, UpdateView):
    model = MiembrosModel
    model_modal = SCientificaModel
    form_class = MiembrosForm
    form_modal = SCientificaForm
    template_name = 'panel/miembros/perfil_miembros.html'
    success_url = reverse_lazy('panel')

    def dispatch(self,request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request,*args, **kwargs)

    def get_object(self):
        id_ = self.request.user.miembro_id
        obj = get_object_or_404(MiembrosModel, id=id_ )
        return obj

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add-scientifica':
                modal = self.model_modal()
                modal.nombre = request.POST['nombre']
                modal.url = request.POST['url']
                modal.desc = request.POST['desc']
                modal.save()
            elif action == 'edit-miembro':
                _instance = self.get_object()
                form = self.form_class(data = request.POST,instance=_instance,files= request.FILES)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Editar Contraseña'
        context['url_panel'] = self.success_url
        context['info'] = {'head_card': 'Editar Perfil Miembro' , 'icono': 'fas fa-edit mr-2'}
        context['modal'] = self.form_modal()
        return context  