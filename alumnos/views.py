from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Prefetch
from django.urls import reverse
from django.core.cache import cache
from alumnos.forms import *
from alumnos.models import *
from notas.models import PdoEscAlum


# Create your views here.

def data_alumnos():

	# lista = cache.get('data_alumnos')
	# if lista is None:
	# 	lista = Alumno.objects.prefetch_related(Prefetch('pdoescalum_set')).all()
	# 	lista = serializers.serialize('json', Alumno.objects.prefetch_related(Prefetch('pdoescalum_set')).all())
	# 	cache.set('data_alumnos', lista)
	# return HttpResponse(json.dumps(data_alumnos()), content_type='application/json')
	# return lista

	lista = Alumno.objects.prefetch_related(Prefetch('pdoescalum_set')).all()

	return lista

@login_required
def AgregarAlumno(request):

	if request.method == "POST":
		form = AlumnoForm(request.POST)
		if form.is_valid():
			alumno = form.save(commit=False)
			alumno.save()
			mensaje = "todo ok"
			return HttpResponseRedirect(reverse('datos_alumno', args=(alumno.id,)))
		else:
			return render(request, 'index.html', {'form' : form})
	else:
		form = AlumnoForm()
		return render(request, 'index.html', {'form' : form})

@login_required
def DatosExtrasAlumno(request, alumnopk):

	alumno = Alumno.objects.get(pk=alumnopk)
	return render(request, 'perfil_alumno.html', {'alumno': alumno})

@login_required
def EditDatosAlumno(request, alumnopk):

	if request.method == 'POST':
		if request.POST.get('form-datos-canaima') == 'on':
			canaima = True
		else:
			canaima = False
		datos = [request.POST.get('form-datos-peso'), canaima, request.POST.get('form-datos-estatura'), request.POST.get('form-datos-talla_c'), request.POST.get('form-datos-talla_p'), request.POST.get('form-datos-talla_z'), request.POST.get('form-datos-telefono')]
		repre = [request.POST.get('form-repres-nombres'), request.POST.get('form-repres-apellidos'), request.POST.get('form-repres-cedula'), request.POST.get('form-repres-nacionalidad'), request.POST.get('form-repres-sexo'), request.POST.get('form-repres-nivel_academico'), request.POST.get('form-repres-telefono'), request.POST.get('form-repres-direccion')]
		pk = Alumno.objects.get(pk=alumnopk)
		form = AlumnoSuperForm(request.POST, instance=pk)
		if form.is_valid():
			alumno = form.save(commit=False)
			alumno.save()
			alum_datos = DatosAlumno.objects.filter(alumno=alumnopk)
			if alum_datos.exists():
				if datos[4] != '' and datos[5] != '':
					alum_datos.update(peso= datos[0], canaima= datos[1], estatura= datos[2], talla_c= datos[3], talla_p= datos[4], talla_z= datos[5], telefono= datos[6], alumno_id= alumnopk)
			else:
				if datos[4] != '' and datos[5] != '':
					agregar = DatosAlumno(peso= datos[0], canaima= datos[1], estatura= datos[2], talla_c= datos[3], talla_p= datos[4], talla_z= datos[5], telefono= datos[6], alumno_id= alumnopk)
					agregar.save()
			alum_repre = RepresenAlumno.objects.filter(alumno=alumnopk)
			if alum_repre.exists():
				if repre[0] != '' and repre[1] != '' and repre[2] != '':
					alum_repre.update(nombres= repre[0], apellidos= repre[1], cedula= repre[2], nacionalidad= repre[3], sexo= repre[4], nivel_academico= repre[5], telefono= repre[6], direccion= repre[7], alumno_id=alumnopk)
			else:
				if repre[0] != '' and repre[1] != '' and repre[2] != '':
					agregar = RepresenAlumno(nombres= repre[0], apellidos= repre[1], cedula= repre[2], nacionalidad= repre[3], sexo= repre[4], nivel_academico= repre[5], telefono= repre[6], direccion= repre[7], alumno_id=alumnopk)
					agregar.save()
			print "todo ok"
		else:
			print "error"
		return render(request, 'perfil_alumno.html', {'alumno': pk, 'mensaje': 'todo ok'})
	else:
		pk = Alumno.objects.get(pk=alumnopk)
		datos = DatosAlumno.objects.filter(alumno=alumnopk)
		alum_repre = RepresenAlumno.objects.filter(alumno=alumnopk)
		var = {}
		var2 = {}
		if datos.exists():
			var = {'peso': datos[0].peso, 'canaima': datos[0].canaima, 'estatura': datos[0].estatura, 'talla_c': datos[0].talla_c, 'talla_p': datos[0].talla_p, 'talla_z': datos[0].talla_z, 'telefono': datos[0].telefono}
		if alum_repre.exists():
			var2 = {'nombres': alum_repre[0].nombres,'apellidos': alum_repre[0].apellidos,'cedula': alum_repre[0].cedula,'nacionalidad': alum_repre[0].nacionalidad,'sexo': alum_repre[0].sexo,'nivel_academico': alum_repre[0].nivel_academico,'telefono': alum_repre[0].telefono,'direccion': alum_repre[0].direccion}
		form = AlumnoSuperForm(instance=pk, initial={'datos': var, 'repres': var2})
		return render(request, 'editar_datos_alumnos.html', {'form': form})

@login_required
def ListaAlumnos(request):

	# print data_alumnos()
	return render(request, 'lista_alumnos.html', {'alumnos' : data_alumnos()})