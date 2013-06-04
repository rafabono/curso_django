from misitio.inventario.models import Servicio, Maquina, SistemaOperativo, Aplicacion, TAplicacion, VAplicacion, Cliente
from django.contrib import admin


class TAplicacionAdmin(admin.ModelAdmin):
        pass

class VAplicacionAdmin(admin.ModelAdmin):
        list_display = ('version', 'taplicacion')

class AplicacionInline(admin.StackedInline):
        model = Aplicacion
        extra = 0
        filter_horizontal = ('maquina',)


class ClienteAdmin(admin.ModelAdmin):
        pass

class ServicioAdmin(admin.ModelAdmin):
        inlines = [ AplicacionInline ]
        list_display = ('nombre', 'descripcion', 'cliente')
        ordering = ('nombre',)
        search_fields = ('nombre', 'descripcion')
        save_on_top = True
        list_per_page = 20

class AplicacionAdmin(admin.ModelAdmin):
        list_display = ('taplicacion', 'descripcion', 'vaplicacion')
        ordering = ('taplicacion',)
        filter_horizontal = ('maquina',)
        save_on_top = True
        list_per_page = 20

class MaquinaAdmin(admin.ModelAdmin):
        list_display = ('nombre', 'ip', 'sistema')
        ordering = ('nombre',)
        save_on_top = True
        list_per_page = 20


class SistemaOperativoAdmin(admin.ModelAdmin):
        list_display = ('nombre',)
        ordering = ('nombre',)
        save_on_top = True
        list_per_page = 20


admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Maquina,MaquinaAdmin)
admin.site.register(Aplicacion,AplicacionAdmin)
admin.site.register(SistemaOperativo,SistemaOperativoAdmin)
admin.site.register(TAplicacion,TAplicacionAdmin)
admin.site.register(VAplicacion,VAplicacionAdmin)
admin.site.register(Cliente,ClienteAdmin)
