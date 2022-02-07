from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import UpdateView, CreateView
from django.views.decorators.csrf import csrf_exempt

from core.web.models import WebModelo
from core.web.forms import PortadaForm



# Para la Portada de la Web
class PortadaCreateView(LoginRequiredMixin,CreateView):
    model = WebModelo
    form_class = PortadaForm
    template_name = 'panel/web/create_portada.html'
    
    # @csrf_exempt
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request,*args, **kwargs)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = PortadaForm(data = request.POST, files= request.FILES) 
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
            

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Panel Administracion'
        context['info'] = {'local': 'Datos de la Web', 'head_card': 'Crear nuevos datos de su Web', 'icono': 'fas fa-plus' }
        return context

class PortadaListView(LoginRequiredMixin,UpdateView):
    model = WebModelo
    form_class = PortadaForm
    template_name = 'panel/web/edit_portada.html'
    
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request,*args, **kwargs)

    def get_object(self):
        query = WebModelo.objects.last()
        if query:
            _id = query.id
            return get_object_or_404(self.model, id=_id)
        else:
            print('create_portada')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            _instance = self.get_object()
            form = self.form_class(data = request.POST,instance=_instance,files= request.FILES)
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)       

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Panel Administracion'
        context['info'] = {'local': 'Datos de la Web', 'head_card': 'Edite los datos de su Web', 'icono': 'fas fa-edit' }
        return context
