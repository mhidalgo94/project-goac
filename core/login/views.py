
from core.login.froms import PwdResetForm
from django.views.generic.edit import FormView
from config import settings
from django.shortcuts import redirect
from django.urls.base import reverse_lazy

from django.contrib.auth.views import LoginView


# Create your views here.
class LoginFormView(LoginView):
    # form_class = AuthenticationForm
    template_name = 'login/login.html'
    success_url = reverse_lazy('panel')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Login'
        
        return context

class PwdResetView(FormView):
    form_class = PwdResetForm
    template_name = 'login/pwd_reset.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = 'GOAC | Restaurar Contraseña'
        
        return context

