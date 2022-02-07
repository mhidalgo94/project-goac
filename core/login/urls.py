from django.urls import path

from core.login.views import LoginFormView, PwdResetView
from django.contrib.auth.views import  LogoutView

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('pass/reset/', PwdResetView.as_view(), name='pwd_reset'),
]
