from django.contrib import admin
from cargar_notas.models import *

# Register your models here.

class AdminPrimeroNTPL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

class AdminPrimeroNTSL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

class AdminPrimeroNTTL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

admin.site.register(PrimeroNTPL, AdminPrimeroNTPL)
admin.site.register(PrimeroNTSL, AdminPrimeroNTSL)
admin.site.register(PrimeroNTTL, AdminPrimeroNTTL)

#  Segundo

class AdminSegundoNTPL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

class AdminSegundoNTSL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

class AdminSegundoNTTL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

admin.site.register(SegundoNTPL, AdminSegundoNTPL)
admin.site.register(SegundoNTSL, AdminSegundoNTSL)
admin.site.register(SegundoNTTL, AdminSegundoNTTL)

# Tercero

class AdminTercerNTPL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

class AdminTercerNTSL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

class AdminTercerNTTL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

admin.site.register(TercerNTPL, AdminTercerNTPL)
admin.site.register(TercerNTSL, AdminTercerNTSL)
admin.site.register(TercerNTTL, AdminTercerNTTL)

# Cuarto

class AdminCuartoNTPL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

class AdminCuartoNTSL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

class AdminCuartoNTTL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

admin.site.register(CuartoNTPL, AdminCuartoNTPL)
admin.site.register(CuartoNTSL, AdminCuartoNTSL)
admin.site.register(CuartoNTTL, AdminCuartoNTTL)

# Quinto

class AdminQuintoNTPL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

class AdminQuintoNTSL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

class AdminQuintoNTTL(admin.ModelAdmin):
	list_display = ('alumno_curso', 'curso', 'docente', 'nota', 'descripcion', 'valor',)

admin.site.register(QuintoNTPL, AdminQuintoNTPL)
admin.site.register(QuintoNTSL, AdminQuintoNTSL)
admin.site.register(QuintoNTTL, AdminQuintoNTTL)