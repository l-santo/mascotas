from django.contrib import admin
from .models import Gallery


#Configuración extendida para mostrar campos quemados
class GalleryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

# Register your models here.

admin.site.register(Gallery,GalleryAdmin)