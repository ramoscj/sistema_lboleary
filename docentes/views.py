from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from django.db.models import Prefetch
from notas.forms import PdoEscSec
from cargar_notas.views import DescargarXls
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required
def RegistrarMaestro(request):

	if request.method == 'POST':
		form = MaestroForm(request.POST)
		if form.is_valid():
			maestro = form.save(commit=False)
			maestro.save()
			form = MaestroForm()
			return render(request, 'registro_docente.html', {'form': form, 'mensaje': 'todo ok'})
		else:
			return render(request, 'registro_docente.html', {'form': form})
	else:
		form = MaestroForm()
		return render(request, 'registro_docente.html', {'form': form})

@login_required
def ListaMaestros(request):

	maestros = Maestro.objects.all().order_by('-cedula')
	return render(request, 'lista_maestros.html', {'maestros': maestros})

@login_required
def EditarMaestro(request, id_docente):

	maestro = get_object_or_404(Maestro, pk=id_docente)
	if request.method == 'POST':
		form = MaestroForm(request.POST, instance=maestro)
		if form.is_valid():
			docente = form.save(commit=False)
			docente.save()
			maestros = Maestro.objects.all().order_by('-cedula')
			return render(request, 'lista_maestros.html', {'mensaje': 'todo ok', 'maestros': maestros})
		else:
			maestros = Maestro.objects.all().order_by('-cedula')
			return render(request, 'lista_maestros.html', {'form': form, 'maestros': maestros})
	else:
		form = MaestroForm(instance=maestro)
		return render(request, 'registro_docente.html', {'form': form})

@login_required
def PeriodoMaterias(request, id_docente):

	form = PdoEscSec()
	docente = get_object_or_404(Maestro, pk=id_docente)
	return render(request, 'lista_periodo.html', {'form': form, 'docente': docente})

@login_required
def MateriasDocente(request, id_docente):

	if request.method == 'POST':
		form = PdoEscSec(request.POST)
		if form.is_valid():
			seleccion = form.save(commit=False)
			maestros = Maestro.objects.filter(pk=id_docente).prefetch_related(Prefetch('materiamaestro_set'))
			if maestros[0].materiamaestro_set.exists():
				datos = {'periodo': maestros[0].materiamaestro_set.all()[0].periodo, 'docente': ('%s %s' % (maestros[0].nombres, maestros[0].apellidos)), 'periodo_pk': maestros[0].materiamaestro_set.all()[0].periodo.id, 'docente_pk': maestros[0].id}
				return render(request, 'lista_maestro_materias.html', {'materias': maestros, 'data_extra': datos})
			else:
				form = PdoEscSec()
				docente = get_object_or_404(Maestro, pk=id_docente)
				return render(request, 'lista_periodo.html', {'form': form, 'docente': docente, 'error': 'error'})
	else: 
		form = PdoEscSec()
		docente = get_object_or_404(Maestro, pk=id_docente)
		return render(request, 'lista_periodo.html', {'form': form, 'docente': docente})