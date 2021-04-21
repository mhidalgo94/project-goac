from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from core.web.models import ContactoModel, NoticiasModels, PublArtArbitrajeModel, PublEventosModel, PublReportesModel
from django.views.generic import TemplateView
from core.servicios.actino.models import ActinoObservadorModel

# Vista Inicio panel
class DashboartListView(LoginRequiredMixin, TemplateView):
    template_name = 'panel/dashboart.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Panel Administracion'
        context['contactos'] = ContactoModel.objects.count()
        context['noticias'] = NoticiasModels.objects.count()
        context['publicaciones'] = PublReportesModel.objects.count()+PublEventosModel.objects.count()+PublArtArbitrajeModel.objects.count()
        context['info'] = {'local': 'Panel Administracion', 'head_card': 'Otros Datos' }
        return context

class ServiciosListView(LoginRequiredMixin, TemplateView):
    template_name = 'panel/servicios/servicios.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Todos Servicios'
        context['info'] = {'local': 'Panel Servicios', 'head_card': 'Servicios','icono': 'fas fa-cogs' }
        context['obv'] = ActinoObservadorModel.objects.all()
        return context


