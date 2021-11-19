from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Favorito)
admin.site.register(Dispositivo)

class ImagenInmuebleAdmin(admin.StackedInline):
    model = ImagenInmueble

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    # cada elemento de esta tupla sera una columna en el admin panel 
    list_display = ('nombre', 'status_de_venta', 'dias_publicado')
    # esto nos permite agregar mas imagenes desde la vista admin del inmueble
    inlines = [ImagenInmuebleAdmin]