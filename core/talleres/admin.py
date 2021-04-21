from django.contrib import admin

from .models import TallerModel, ParticipantesTallerModel, ResumenesTallerModel


# Register your models here.
admin.site.register(TallerModel)
admin.site.register(ParticipantesTallerModel)
admin.site.register(ResumenesTallerModel)