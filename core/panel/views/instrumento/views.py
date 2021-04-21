from django.contrib import messages
from django.shortcuts import redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView
from django.views.decorators.csrf import csrf_exempt

from core.web.models import  InstrumentoModel
from core.web.forms import  InstrumentoForm



# Instrumentos
class InstrumentoListView(LoginRequiredMixin,ListView):
    template_name = 'panel/instrumento/list_instrumento.html'
    model = InstrumentoModel

    def get_object(self):
        query = self.model.objects.all()
        return query

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request,*args,**kwargs)

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
        context['titulo'] = 'GOAC | Lista Instrumento'
        context['info'] = {'local': 'Panel de Instrumentos', 'head_card': 'Datos Instrumentos', 'icono': 'fas fa-search' }
        return context


class InstrumentoCreateView(LoginRequiredMixin,CreateView):
    model = InstrumentoModel
    form_class = InstrumentoForm
    template_name = 'panel/instrumento/create_instrumento.html'
    success_url = reverse_lazy('list_instrumento')


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Crear Instrumento'
        context['info'] = {'local': 'Panel Instrumentos', 'head_card': 'Crear Instrumento' , 'icono': 'fas fa-plus'}
        return context

# Arreglar Detalles de Updates
class InstrumentoUpdateView(LoginRequiredMixin,UpdateView):
    model = InstrumentoModel
    form_class = InstrumentoForm
    template_name = 'panel/instrumento/edit_instrumento.html'
    success_url = reverse_lazy('list_instrumento')


    def dispatch(self,request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        self.object = self.get_object()
        return super().dispatch(request,*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Editar Instrumento'
        context['info'] = {'local': 'Panel Instrumentos', 'head_card': 'Actualizar Instrumento', 'icono': 'fas fa-edit' }
        return context    

