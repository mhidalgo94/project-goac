from django.contrib.auth.mixins import LoginRequiredMixin
from core.web.forms import NoticiasForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,  UpdateView, CreateView
from django.views.decorators.csrf import csrf_exempt


from core.web.models import NoticiasModels

# Noticias Sitio
class NoticiasListView(LoginRequiredMixin,ListView):
    model = NoticiasModels
    template_name = 'panel/noticias/list_noticias.html'


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
        context['titulo'] = 'GOAC | Lista de Noticias '
        context['info'] = {'head_card': 'Noticias', 'icono': 'fas fa-newspaper' }
        return context


class NoticiasCreateView(LoginRequiredMixin,CreateView):
    model = NoticiasModels
    form_class = NoticiasForm
    template_name = 'panel/noticias/create_noticias.html'
    success_url = reverse_lazy('list_noticias')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Crear Noticias'
        context['info'] = {'head_card': 'Crear Noticias' , 'icono': 'fas fa-plus mr-2'}
        return context

class NoticiasUpdateView(LoginRequiredMixin,UpdateView):
    model = NoticiasModels
    form_class = NoticiasForm
    template_name = 'panel/noticias/edit_noticias.html'
    success_url = reverse_lazy('list_noticias')


    def dispatch(self,request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request,*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Editar Noticias'
        context['info'] = {'head_card': 'Actualizar Noticia', 'icono': 'fas fa-edit' }
        return context    

