from django.contrib import admin
from .models import *
from notas.forms import *
# Register your models here.

class AdminAlumnos(admin.ModelAdmin):
	list_display = ('nombres', 'apellidos', 'cedula', 'sexo', 'fchanac',)

class AdminMaterias(admin.ModelAdmin):
	list_display = ('nombre', 'nombcorto',)

class AdminPeriodo(admin.ModelAdmin):
	list_display = ('periodo', 'codigo',)

class AdminPdoEscAlum(admin.ModelAdmin):
	list_display = ('alumno', 'periodo', 'asignado',)

class AdminPdoGradoSec(admin.ModelAdmin):
	list_display = ('grado','seccion', 'periodo',)

class AdminCodigoMateria(admin.ModelAdmin):
	list_display = ('codigo',)

class AdminCodigoMateria(admin.ModelAdmin):
	filter_horizontal = ('m_primero', 'm_segundo', 'm_tercero', 'm_cuarto','m_quinto',)


admin.site.register(Alumno, AdminAlumnos)
admin.site.register(Materia, AdminMaterias)
admin.site.register(PeriodoEscolar, AdminPeriodo)
admin.site.register(PdoEscAlum, AdminPdoEscAlum)
admin.site.register(PdoGradoSec, AdminPdoGradoSec)
admin.site.register(CodigoMateria, AdminCodigoMateria)
