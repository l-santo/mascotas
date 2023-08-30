from django.contrib import admin
from .models import Service


#Configuración extendida para mostrar campos quemados
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


# Register your models here.
admin.site.register(Service,ServiceAdmin)