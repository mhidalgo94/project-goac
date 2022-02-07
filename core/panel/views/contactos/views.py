from django.contrib import messages
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

from core.web.models import  ContactoModel


# Lista de los Contactos de la Web
class ContactoListView(LoginRequiredMixin,ListView):
    template_name = 'panel/contacto/list_contacto.html'
    model = ContactoModel

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request,*args,**kwargs)

    def get_object(self):
        query = self.model.objects.all()
        return query


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
        context['titulo'] = 'GOAC | Lista Contactos'
        context['info'] = {'local': 'Datos de Contactos', 'head_card': 'Contactos', 'icono': 'fas fa-list' }
        return context
