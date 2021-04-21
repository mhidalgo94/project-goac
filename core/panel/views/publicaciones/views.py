from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from core.web.forms import PublArtArbitrajeForm, PublEventosForm, PublReportesForm
from django.http import JsonResponse
from django.views.generic import UpdateView, CreateView, ListView
from django.views.decorators.csrf import csrf_exempt

from core.web.models import PublArtArbitrajeModel, PublReportesModel, PublEventosModel

# Reportes de Publicaciones del Sitio
class PublReportesListView(LoginRequiredMixin,ListView):
    model = PublReportesModel
    template_name = 'panel/publicaciones/reportes/list_reportes.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
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
        context['titulo'] = 'GOAC | Publicaciones |Lista de Reportes'
        context['info'] = {'head_card': 'Publicaciones | Reportes', 'icono': 'fas fa-bookmark' }
        return context


class PublReportesCreateView(LoginRequiredMixin,CreateView):
    model = PublReportesModel
    form_class = PublReportesForm
    template_name = 'panel/publicaciones/reportes/create_reportes.html'
    success_url = reverse_lazy('list_reportes')
    
    
    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Publicaciones | Reportes'
        context['info'] = {'head_card': 'Publicaciones | Crear Reportes', 'icono': 'fas fa-plus' }
        return context

class PublReportesUpdateView(LoginRequiredMixin,UpdateView):
    model = PublReportesModel
    form_class = PublReportesForm
    template_name = 'panel/publicaciones/reportes/edit_reportes.html'
    success_url = reverse_lazy('list_reportes')
   

    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Publicaciones |Actualizar de Reportes'
        context['info'] = { 'head_card': 'Publicaciones | Actualizar Reportes', 'icono': 'fas fa-edit' }
        return context


# Articulos y Arbitrajes de Publicaciones del Sitio
class PublArtArbitrajeListView(LoginRequiredMixin,ListView):
    model = PublArtArbitrajeModel
    template_name = 'panel/publicaciones/arbitraje/list_arbitrajes.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
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
        context['titulo'] = 'GOAC | Publicaciones | Lista de Articulos e Arbitrajes'
        context['info'] = {'head_card': 'Publicaciones | Articulos con Arbitrajes', 'icono': 'fas fa-bookmark' }
        return context


class PublArtArbitrajeCreateView(LoginRequiredMixin,CreateView):
    model = PublArtArbitrajeModel
    form_class = PublArtArbitrajeForm
    template_name = 'panel/publicaciones/arbitraje/create_arbitrajes.html'
    success_url = reverse_lazy('list_arbitraje')
    

    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Publicaciones | Crear Articulos e Arbitrajes'
        context['info'] = {'head_card': 'Publicaciones | Crear Articulos con Arbitrajes', 'icono': 'fas fa-plus' }
        return context

class PublArtArbitrajeUpdateView(LoginRequiredMixin,UpdateView):
    model = PublArtArbitrajeModel
    form_class = PublArtArbitrajeForm
    template_name = 'panel/publicaciones/arbitraje/edit_arbitrajes.html'
    success_url = reverse_lazy('list_arbitraje')


    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Publicaciones | Actualizar Articulos con Arbitrajes'
        context['info'] = { 'head_card': 'Publicaciones | Actualizar Reportes', 'icono': 'fas fa-edit' }
        return context


# Articulos y Arbitrajes de Publicaciones del Sitio
class PublEventosModelListView(LoginRequiredMixin,ListView):
    model = PublEventosModel
    template_name = 'panel/publicaciones/eventos/list_eventos.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
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
        context['titulo'] = 'GOAC | Publicaciones | Lista de Eventos'
        context['info'] = {'head_card': 'Publicaciones | Eventos', 'icono': 'fas fa-bookmark' }
        return context


class PublEventosModelCreateView(LoginRequiredMixin,CreateView):
    model = PublEventosModel
    form_class = PublEventosForm
    template_name = 'panel/publicaciones/eventos/create_eventos.html'
    success_url = reverse_lazy('list_eventos')
    

    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Publicaciones | Crear Evento'
        context['info'] = {'head_card': 'Publicaciones | Crear Evento', 'icono': 'fas fa-plus' }
        return context

class PublEventosUpdateView(LoginRequiredMixin,UpdateView):
    model = PublEventosModel
    form_class = PublEventosForm
    template_name = 'panel/publicaciones/eventos/edit_eventos.html'
    success_url = reverse_lazy('list_eventos')
   

    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Publicaciones | Actualizar Eventos'
        context['info'] = { 'head_card': 'Publicaciones | Actualizar Evento', 'icono': 'fas fa-edit' }
        return context