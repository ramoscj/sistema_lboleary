from __future__ import unicode_literals
from django.db import models
from notas.models import PdoEscAlum 
from docentes.models import MateriaMaestro, Maestro

# Primero

class PrimeroNTPL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()

class PrimeroNTSL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()

class PrimeroNTTL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()

# Segudo

class SegundoNTPL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()

class SegundoNTSL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()

class SegundoNTTL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()

# Tercer

class TercerNTPL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()

class TercerNTSL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()

class TercerNTTL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()

# Cuarto

class CuartoNTPL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()

class CuartoNTSL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()

class CuartoNTTL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()

# Quinto

class QuintoNTPL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()

class QuintoNTSL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()

class QuintoNTTL(models.Model):

	alumno_curso = models.ForeignKey(PdoEscAlum)
	curso = models.ForeignKey(MateriaMaestro)
	docente = models.ForeignKey(Maestro)
	nota = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=140)
	valor = models.PositiveSmallIntegerField()