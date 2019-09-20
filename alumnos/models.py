from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Alumno(models.Model):

	genero = (
		('M','Masculino'),
		('F','Femenino'),
	)

	nacionalidades = (
		('V', 'Venezolana'),
		('E', 'Extranjera'),
	)

	estados = (
		('AMAZONAS', 'AMAZONAS'),
		('ANZOATEGUI', 'ANZOATEGUI'),
		('APURE', 'APURE'),
		('ARAGUA', 'ARAGUA'),
		('BARINAS', 'BARINAS'),
		('BOLIVAR', 'BOLIVAR'),
		('CARABOBO', 'CARABOBO'),
		('COJEDES', 'COJEDES'),
		('DELTA AMACURO', 'DELTA AMACURO'),
		('DISTRITO CAPITAL', 'DISTRITO CAPITAL'),
		('FALCON', 'FALCON'),
		('GUARICO', 'GUARICO'),
		('LARA', 'LARA'),
		('MERIDA', 'MERIDA'),
		('MIRANDA', 'MIRANDA'),
		('MONAGAS', 'MONAGAS'),
		('NUEVA ESPARTA', 'NUEVA ESPARTA'),
		('PORTUGUESA', 'PORTUGUESA'),
		('SUCRE', 'SUCRE'),
		('TACHIRA', 'TACHIRA'),
		('TRUJILLO', 'TRUJILLO'),
		('VARGAS', 'VARGAS'),
		('YARACUY', 'YARACUY'),
		('ZULIA', 'ZULIA'),
		('OTRO PAIS', 'OTRO PAIS'),
	)

	nombres = models.CharField(max_length=140)
	apellidos = models.CharField(max_length=140)
	nacionalidad = models.CharField(max_length=10, choices=nacionalidades)
	cedula = models.CharField(max_length=50, unique=True)
	sexo = models.CharField(max_length=140, choices=genero)
	fchanac = models.DateField()
	lugarnac = models.CharField(max_length=50, choices=estados, blank=True)
	correo = models.EmailField(max_length=140, blank=True)
	creado = models.DateField(auto_now=True)

	def __unicode__(self):
		return str(self.cedula)

class DatosAlumno(models.Model):

	tallas = (
		('10', '10'),
		('12', '12'),
		('14', '14'),
		('16', '16'),
		('S', 'S'),
		('SS', 'SS'),
		('M', 'M'),
		('L', 'L'),
		('XL', 'XL'),
	)
	alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
	peso = models.CharField(max_length=5, blank=True, null=True)
	canaima = models.BooleanField(blank=True)
	estatura = models.CharField(max_length=5, blank=True, null=True)
	talla_c = models.CharField(max_length=50, blank=True, null=True, choices=tallas)
	talla_z = models.IntegerField(default=0, blank=True, null=True)
	talla_p = models.IntegerField(default=0, blank=True, null=True)
	foto = models.ImageField(upload_to='perfil/alumnos/')
	telefono = models.CharField(max_length=50, blank=True, null=True)

	def __unicode__(self):
		return str(self.alumno)

class RepresenAlumno(models.Model):

	genero = (
		('M','Masculino'),
		('F','Femenino'),
	)

	nacionalidades = (
		('V', 'Venezolana'),
		('E', 'Extranjera'),
	)

	niveles = (
		('Primaria','Primaria'),
		('Bachiller','Bachiller'),
		('Universitario','Universitario'),
		('Maestria','Maestria'),
		('Especialista','Especialista'),
		('Doctor','Doctor'),
		('Ninguno','Ninguno'),
	)

	alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
	nombres = models.CharField(max_length=140, null=True, blank=True)
	apellidos = models.CharField(max_length=140, null=True, blank=True)
	nacionalidad = models.CharField(max_length=20,choices=nacionalidades, blank=True)
	cedula = models.IntegerField(null=True, blank=True)
	sexo = models.CharField(max_length=20, choices=genero, blank=True)
	nivel_academico = models.CharField(max_length=50, choices=niveles, blank=True)
	telefono = models.CharField(max_length=50, blank=True, null=True)
	direccion = models.TextField(blank=True, null=True)