from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,  UpdateView, CreateView

from core.web.models import CatInvestigacionesModel, InvestigacionesModel
from core.web.forms import CatInvestigacionForm, InvestigacionesForm

# Investigaciones
class InvestigacionesListView(LoginRequiredMixin,ListView):
    model = InvestigacionesModel
    template_name = 'panel/investigaciones/list_investigaciones.html'

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
        context['titulo'] = 'GOAC | Lista de Investigaciones'
        context['info'] = {'head_card': 'Investigaciones', 'icono': 'fa fa-university' }
        return context


class InvestigacionesCreateView(LoginRequiredMixin,CreateView):
    model = InvestigacionesModel
    model_modal = CatInvestigacionesModel
    form_class = InvestigacionesForm
    form_modal = CatInvestigacionForm
    template_name = 'panel/investigaciones/create_investigaciones.html'
    success_url = reverse_lazy('list_investigaciones')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Lista de Investigaciones'
        context['info'] = {'head_card': 'Agregar Investigaciones' , 'icono': 'fas fa-plus mr-2'}
        context['modal'] = self.form_modal()
        return context

class InvestigacionUpdateView(LoginRequiredMixin,UpdateView):
    model = InvestigacionesModel
    model_modal = CatInvestigacionesModel
    form_class = InvestigacionesForm
    form_modal = CatInvestigacionForm
    template_name = 'panel/investigaciones/edit_investigaciones.html'
    success_url = reverse_lazy('list_investigaciones')


    def dispatch(self,request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request,*args, **kwargs)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Editar Miembro'
        context['info'] = {'head_card': 'Actualizar Investigaciones', 'icono': 'fas fa-edit' }
        # context['form'] = self.form_class()
        context['modal'] = self.form_modal()
        return context    


# Categorias de Investigaciones
class CategoriasInvListView(LoginRequiredMixin,ListView):
    model = CatInvestigacionesModel
    model_modal = CatInvestigacionesModel
    form_modal = CatInvestigacionForm
    template_name = 'panel/investigaciones/categorias/list_categorias.html'

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
            elif action == 'create-catinvest':
                form = self.form_modal(request.POST)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            elif action== 'edit-catinvest':
                cat = self.model.objects.get(id=request.POST['id'])
                cat.nombre = request.POST['nombre']
                cat.save()
            elif action== 'eliminar':
                id_ = request.POST['id']
                m = self.model.objects.get(id=id_)
                m.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Lista de Categorias de Investigaciones'
        context['info'] = {'head_card': 'Categorias de Investigaciones', 'icono': 'fa fa-flag' }
        context['modal'] = self.form_modal()
        return context
