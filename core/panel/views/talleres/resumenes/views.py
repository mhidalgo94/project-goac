from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from core.talleres.models import ResumenesTallerModel, TallerModel
from core.talleres.forms import ResumenesTForm



class ResumenesTListView(LoginRequiredMixin, ListView):
    template_name = 'panel/talleres/resumenes/list_resumenes.html'
    model = ResumenesTallerModel

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
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Talleres"
        context['info'] = {'head_card': 'Lista de Resumenes', 'icono': 'fas fa-clipboard-check' }
        return context


class ResumenesTCreateView(LoginRequiredMixin, CreateView):
    model = ResumenesTallerModel
    form_class = ResumenesTForm
    template_name = 'panel/talleres/resumenes/create_resumenes.html'
    success_url = reverse_lazy('list_resumenes')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Talleres"
        context['info'] = {'head_card': 'Taller | Crear Resumenes', 'icono': 'fas fa-paste' }
        return context


class ResumenesTUpdateView(LoginRequiredMixin, UpdateView):
    model = ResumenesTallerModel
    form_class = ResumenesTForm
    template_name = 'panel/talleres/resumenes/edit_resumenes.html'
    success_url = reverse_lazy('list_resumenes')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Talleres"
        context['info'] = {'head_card': 'Taller | Editar Resumenes', 'icono': 'fas fa-paste' }
        return context