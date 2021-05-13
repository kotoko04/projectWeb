from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')

class listaServicioAdmin(admin.ModelAdmin):
    list_display = ("titulo",)

admin.site.register(Servicio, ServicioAdmin)