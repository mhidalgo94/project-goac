from django.contrib import admin

from core.miembros.models import MiembrosModel, SCientificaModel


# Register your models here.
admin.site.register(MiembrosModel)
admin.site.register(SCientificaModel)