from __future__ import unicode_literals
from django.db import models
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey
from notas.models import PdoGradoSec, Materia, PeriodoEscolar

# Create your models here.

class Maestro(models.Model):

	genero = (
		('M','Masculino'),
		('F','Femenino'),
	)

	nacionalidades = (
		('V', 'Venezolana'),
		('E', 'Extranjera'),
	)

	nombres = models.CharField(max_length=140)
	apellidos = models.CharField(max_length=140)
	cedula = models.IntegerField(unique=True)
	sexo = models.CharField(max_length=140, choices=genero)
	fchanac = models.DateField()
	creado = models.DateField(auto_now=True)
	foto = models.ImageField(upload_to='perfil/docentes/')
	correo = models.EmailField()
	nacionalidad = models.CharField(max_length=50, choices=nacionalidades) 

	def __unicode__(self):
		return ("%s %s") % (self.nombres, self.apellidos)

class MateriaMaestro(models.Model):

	maestro = models.ForeignKey(Maestro)
	materia = models.ForeignKey(Materia)
	periodo = models.ForeignKey(PeriodoEscolar)
	seccion = ChainedForeignKey(
        'notas.PdoGradoSec',
        chained_field="periodo",
        chained_model_field="periodo",
        show_all=False,
        auto_choose=True,
        blank=False,
        null=False
    )

	def __unicode__(self):
		return ("Doc:%s-%s-%s") % (self.maestro.cedula, self.materia.nombre, self.seccion)