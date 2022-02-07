from django.contrib import admin

from .models import WebModelo, ContactoModel, NoticiasModels, PublArtArbitrajeModel, PublEventosModel, PublReportesModel, CatInvestigacionesModel, InvestigacionesModel, InstrumentoModel

# Register your models here.
admin.site.register(WebModelo)
admin.site.register(InstrumentoModel)
admin.site.register(ContactoModel)
admin.site.register(NoticiasModels)
admin.site.register(PublArtArbitrajeModel)
admin.site.register(PublEventosModel)
admin.site.register(PublReportesModel)
admin.site.register(CatInvestigacionesModel)
admin.site.register(InvestigacionesModel)
