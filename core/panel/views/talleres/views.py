from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from datetime import datetime

from core.talleres.models import ResumenesTallerModel, TallerModel
from core.talleres.forms import TallerForm


class TallerListView(LoginRequiredMixin, ListView):
    template_name = 'panel/talleres/todos_talleres/todos_talleres.html'
    queryset = TallerModel.objects.all().order_by('-id')
    model = TallerModel

    def post(self,request,*args,**kwargs):
        busqueda = request.POST['buscar'] 
        objects = self.model.objects.filter(Q(titulo__icontains=busqueda)|Q(descripcion__icontains=busqueda)).distinct().order_by('-id')
        context ={
            'titulo' : "GOAC | Lista de Talleres",
            'info': {'head_card': 'Lista de Talleres', 'icono': 'fas fa-wrench' },
            'object_list': objects,
            'busqueda':busqueda
        }
        return render(request,self.template_name, context)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Lista de Talleres"
        context['info'] = {'head_card': 'Lista de Talleres', 'icono': 'fas fa-wrench' }
        return context


class TallerCreateView(LoginRequiredMixin, CreateView):
    model = TallerModel
    form_class = TallerForm
    template_name = 'panel/talleres/crear_taller/create_taller.html'
    success_url = reverse_lazy('list_talleres')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Editar de Talleres"
        context['info'] = {'head_card': 'Crear Nuevo Taller', 'icono': 'fas fa-plus' }
        return context


class TallerUpdateView(LoginRequiredMixin, UpdateView):
    model = TallerModel
    form_class = TallerForm
    template_name = 'panel/talleres/edit_taller/edit_taller.html'
    success_url = reverse_lazy('list_talleres')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST.get('action')
            pk_ = request.POST.get('pk')
            qry = self.model.objects.get(pk=pk_)

            if action == 'taller':
                qry.titulo = request.POST['titulo']
                qry.fecha_inicio = datetime.strptime(request.POST['fecha_inicio'], '%d/%m/%Y')
                qry.fecha_culmina = datetime.strptime(request.POST['fecha_culmina'], '%d/%m/%Y')
                qry.descripcion = request.POST['descripcion']                
                qry.genesis = request.POST['genesis']
                qry.save()
                return redirect(self.success_url)
            elif action == 'programas':
                qry.programa = request.POST['programa']
                try:
                    qry.save()
                    return redirect(self.success_url)
                except Exception as e:
                    data['error'] = str(e)
            elif action == 'participantes':
                qry.participantes.clear()
                qry.participantes.set(request.POST.getlist('participantes'))
                qry.save()
                return redirect(self.success_url)
            elif action == 'eliminar':
                self.model.objects.get(pk=pk_)
                qry.delete()
            else:
                data['error'] = 'Ha ocurrido un error'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False) 


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "GOAC | Editar Taller"
        context['info'] = {'head_card': 'Editar Taller', 'icono': 'fas fa-edit' }
        context['resumenes'] = ResumenesTallerModel.objects.filter(taller__pk=self.kwargs.get('pk'))
        return context