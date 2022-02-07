from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic.edit import FormView
from core.usuarios.forms import UsuariosForm, UsuariosPerfilForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,  UpdateView, CreateView
from core.usuarios.models import Usuarios

# Usuarios
class UsuariosListView(LoginRequiredMixin,ListView):
    model = Usuarios
    template_name = 'panel/usuarios/list_usuarios.html'

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
            elif action== 'eliminar':
                id_ = request.POST['id']
                m = self.model.objects.get(id=id_)
                m.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Lista de Usuarios'
        context['info'] = {'head_card': 'Usuarios', 'icono': 'fas fa-users-cog' }
        return context


class UsuariosCreateView(LoginRequiredMixin,CreateView):
    model = Usuarios
    form_class = UsuariosForm
    template_name = 'panel/usuarios/create_usuarios.html'
    success_url = reverse_lazy('list_usuarios')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder a usuarios')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Agregar Usuario'
        context['info'] = {'head_card': 'Agregar Usuario' , 'icono': 'fas fa-user-plus mr-2'}
        return context

class UsuariosUpdateView(LoginRequiredMixin,UpdateView):
    model = Usuarios
    form_class = UsuariosForm
    template_name = 'panel/usuarios/edit_usuarios.html'
    success_url = reverse_lazy('list_usuarios')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder a usuarios')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Editar Usuario'
        context['info'] = {'head_card': 'Editar Usuario' , 'icono': 'fas fa-user-cog mr-2'}
        return context  


class PerfilUpdateView(LoginRequiredMixin,UpdateView):
    model = Usuarios
    form_class = UsuariosPerfilForm
    template_name = 'panel/usuarios/perfil/edit_perfil.html'
    success_url = reverse_lazy('panel')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Editar Perfil'
        context['info'] = {'head_card': 'Editar Perfil' , 'icono': 'fas fa-user-cog mr-2'}
        return context  

class PefilEditPwdView(LoginRequiredMixin, FormView):
    model = Usuarios
    form_class = PasswordChangeForm
    template_name = 'panel/usuarios/perfil/edit_pwd.html'
    success_url = reverse_lazy('login')


    def get_form(self, form_class=None):
        form = PasswordChangeForm(user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = PasswordChangeForm(user = request.user, data= request.POST) 
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Editar Contraseña'
        context['url_panel'] = self.success_url
        context['info'] = {'head_card': 'Editar Contraseña' , 'icono': 'fas fa-user-shield mr-2'}
        return context  