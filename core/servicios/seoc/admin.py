from django.contrib import admin

from .models import SeocModel, SeocAPIToken

# Register your models here.
admin.site.register(SeocModel)
admin.site.register(SeocAPIToken)