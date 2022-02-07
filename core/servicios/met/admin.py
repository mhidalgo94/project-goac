from django.contrib import admin

from core.servicios.met.models import MetModel, MetAPITokenModel, MetHistoricosModel

# Register your models here.
admin.site.register(MetModel)
admin.site.register(MetAPITokenModel)
admin.site.register(MetHistoricosModel)