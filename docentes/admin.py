from django.contrib import admin
from docentes.models import *

# Register your models here.

class AdminMaestro(admin.ModelAdmin):
	list_display = ('nombres', 'apellidos', 'cedula', 'sexo', 'fchanac', 'correo',)

class AdminMateriaMaestro(admin.ModelAdmin):
	list_display = ('maestro','materia','periodo','seccion',)

admin.site.register(Maestro, AdminMaestro)
admin.site.register(MateriaMaestro, AdminMateriaMaestro)