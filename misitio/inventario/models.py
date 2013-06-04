from django.db import models
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

class Cliente(models.Model):
    	nombre = models.CharField(max_length=200, unique=True, verbose_name='Cliente')
    	descripcion = models.TextField()

    	def __str__(self):
                return self.nombre
    	class Meta:
                ordering = ['nombre']
                verbose_name_plural = "Clientes"

class Servicio(models.Model):
        nombre = models.CharField(max_length=200, unique=True, verbose_name='Servicio')
        descripcion = models.TextField()
        cliente = models.ForeignKey(Cliente, null=True)
      
        def __str__(self):
                return self.nombre
        class Meta:
                ordering = ['nombre']


class TAplicacion(models.Model):
    	nombre = models.CharField(max_length=200, unique=True, verbose_name='Tipo Aplicacion')

        def __str__(self):
                return self.nombre

        class Meta:
                ordering = ['nombre']
        verbose_name_plural = "Tipos de Aplicaciones"


class VAplicacion(models.Model):
    	version = models.CharField(max_length=200, unique=False, verbose_name='Version de aplicacion')
    	taplicacion = models.ForeignKey(TAplicacion)
        def __str__(self):
                return self.version

        class Meta:
                ordering = ['version']
        verbose_name_plural = "Versiones de Aplicaciones"


class SistemaOperativo(models.Model):
        nombre = models.CharField(max_length=200, unique=True, verbose_name='Sistema Operativo')

        def __str__(self):
                return self.nombre
        class Meta:
                ordering = ['nombre']
        verbose_name_plural = "Sistemas Operativos"


class Maquina(models.Model):
        nombre = models.CharField(max_length=200, unique=True, verbose_name='Maquina')
        ip = models.IPAddressField()
    	sistema = models.ForeignKey(SistemaOperativo)

        def __str__(self):
                return self.nombre
    	class Meta:
        	ordering = ['nombre']


class Aplicacion(models.Model):
    	taplicacion = models.ForeignKey(TAplicacion, verbose_name="Tipo Aplic", help_text="Selecciona el tipo de aplicacion")
        vaplicacion= ChainedForeignKey(VAplicacion, chained_field="taplicacion", chained_model_field="taplicacion", verbose_name="Version de Aplic", help_text="Selecciona la version de la aplicacion")
    	descripcion = models.TextField(help_text="Descripcion de la aplicacion")
        ruta = models.CharField(max_length=200, unique=False, verbose_name="Ruta instalacion", help_text="Donde esta instalado")
    	maquina = models.ManyToManyField(Maquina)
    	servicio = models.ForeignKey(Servicio, verbose_name='Servicios')
   
    	def _get_tvaplicacion(self):
        	return '%s %s' % (self.taplicacion,self.vaplicacion)
    	class Meta:
                ordering = ['taplicacion']
                verbose_name_plural = "Aplicaciones"
    	tvaplicacion = property(_get_tvaplicacion)
