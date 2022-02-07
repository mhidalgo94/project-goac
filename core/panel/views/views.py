import subprocess
from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt

from core.web.models import ContactoModel, NoticiasModels, PublArtArbitrajeModel, PublEventosModel, PublReportesModel
from django.views.generic import TemplateView
from core.servicios.actino.models import ActinoObservadorModel
from core.servicios_control import leer_estado_servicios, escribir_estado_servicios


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
        cant_publ = PublReportesModel.objects.count()+PublEventosModel.objects.count()+PublArtArbitrajeModel.objects.count()
        context['publicaciones'] = cant_publ
        context['info'] = {'local': 'Panel Administracion', 'head_card': 'Otros Datos' }
        return context


class ServiciosListView(LoginRequiredMixin, TemplateView):
    template_name = 'panel/servicios/servicios.html'

    # @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            messages.error(request, 'No tienes permisos suficiente para acceder')
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)

    def post(self,request, *args, **kwargs):
        data={}
        try:
            servicios = leer_estado_servicios()
            accion = request.POST.get('accion')
            if accion == 'check-servicios':
                data['servicios'] = servicios
            elif accion == 'activar-servicio':
                post_servicio = request.POST['servicio']
                post_valor = request.POST['valor']
                valor = True if post_valor =='true' else False
                servicios[post_servicio] = valor
                escribir_estado_servicios(servicios)
            
        except FileNotFoundError:
            data['warning_file'] = 'El archivo "Control de Servicios" no existe,presione "Ok" para restablecer.Debe activar los servicios manualmente'
            escribir_estado_servicios({'actino': False, 'met': False, 'seoc': False, 'pyra_par': False})

        except Exception as e:
            data['error']= str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Todos Servicios'
        context['info'] = {'local': 'Panel Servicios', 'head_card': 'Servicios','icono': 'fas fa-cogs' }
        context['obv'] = ActinoObservadorModel.objects.all()
        return context

class EjectView(LoginRequiredMixin,TemplateView):
    template_name = 'panel/eject.html'

    def post(self,request,*args,**kwargs):
        data = {}
        try:
            data['output'] = list()
            command = request.POST.get('command')
            value = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for output in value.stdout.readlines():
                data['output'].append(output.decode('utf-8').strip('\n'))
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Ejecutar'
        context['info'] = {'local': 'Ejecutar', 'head_card': 'Ejecutar Virtual','icono': 'fas fa-play' }
        context['obv'] = ActinoObservadorModel.objects.all()
        return context
