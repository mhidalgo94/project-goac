from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from core.talleres.models import ParticipantesTallerModel, TallerModel
from core.talleres.forms import ParticipantesTallerForm



class ParticipanteTListView(LoginRequiredMixin, ListView):
    template_name = 'panel/talleres/participantes/list_participantes.html'
    model = ParticipantesTallerModel
    queryset = ParticipantesTallerModel.objects.all().order_by('-id')

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
        context['info'] = {'head_card': 'Lista de Participantes', 'icono': 'fas fa-users' }
        return context


class ParticipanteTCreateView(LoginRequiredMixin, CreateView):
    model = ParticipantesTallerModel
    form_class = ParticipantesTallerForm
    template_name = 'panel/talleres/participantes/create_participantes.html'
    success_url = reverse_lazy('list_participantes')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Talleres"
        context['info'] = {'head_card': 'Taller | Crear Participantes', 'icono': 'fas fa-users' }
        return context


class ParticipanteTUpdateView(LoginRequiredMixin, UpdateView):
    model = ParticipantesTallerModel
    form_class = ParticipantesTallerForm
    template_name = 'panel/talleres/participantes/edit_participantes.html'
    success_url = reverse_lazy('list_participantes')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Talleres"
        context['info'] = {'head_card': 'Taller | Editar Participantes', 'icono': 'fas fa-users' }
        return context