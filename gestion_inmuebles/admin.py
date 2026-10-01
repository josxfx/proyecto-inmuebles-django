from django.contrib import admin
from .models import Inmueble, Region, Comuna


class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'comuna', 'tipo_inmueble', 'precio_mensual')
    search_fields = ('nombre', 'descripcion', 'direccion')
    list_filter = ('tipo_inmueble', 'comuna', 'precio_mensual')


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'region')
    search_fields = ('nombre',)
    list_filter = ('region',)


admin.site.register(Inmueble, InmuebleAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Comuna, ComunaAdmin)