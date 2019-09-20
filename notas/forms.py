from django.contrib.admin.widgets import FilteredSelectMultiple
from django.conf import settings
from django import forms 
from .models import *
from django.contrib.auth.models import User
from django_superform import SuperModelForm, ModelFormField, ForeignKeyFormField


class PdoEscAlumForm(forms.ModelForm):

	class Meta:
		model = PdoEscAlum
		fields = ('periodo', 'asignado', 'condicion', 'materiap',)

	def __init__(self, *args, **kwargs):
		super(PdoEscAlumForm, self).__init__(*args, **kwargs)
		self.fields['periodo'].widget.attrs.update({'class': 'form-control',})
		self.fields['asignado'].widget.attrs.update({'class': 'form-control',})
		self.fields['condicion'].widget.attrs.update({'class': 'form-control',})
		self.fields['materiap'].widget.attrs.update({'class': 'form-control',})

	class Media:
		extend = False
		js = ('jquery.init.js', 'chainedfk.js', 'bindfields.js', 'jquery.min.js',)

class PdoEditAlum(forms.ModelForm):

	class Meta:
		model = PdoEscAlum
		fields = ('alumno', 'periodo', 'asignado', 'condicion', 'materiap',)

	def __init__(self, *args, **kwargs):
		super(PdoEditAlum, self).__init__(*args, **kwargs)
		self.fields['alumno'].widget.attrs.update({'hidden': 'true',})
		self.fields['periodo'].widget.attrs.update({'hidden': 'true',})
		self.fields['asignado'].widget.attrs.update({'class': 'form-control',})
		self.fields['condicion'].widget.attrs.update({'class': 'form-control',})
		self.fields['materiap'].widget.attrs.update({'class': 'form-control',})

class PdoEscSec(forms.ModelForm):

	class Meta:
		model = PdoEscAlum
		fields = ('periodo',)

	def __init__(self, *args, **kwargs):
		super(PdoEscSec, self).__init__(*args, **kwargs)
		self.fields['periodo'].widget.attrs.update({'class': 'form-control',})

class AsigDocSecForm(forms.ModelForm):

	class Meta:
		model = PdoEscAlum
		fields = ('periodo', 'asignado',)

	def __init__(self, *args, **kwargs):
		super(AsigDocSecForm, self).__init__(*args, **kwargs)
		self.fields['periodo'].widget.attrs.update({'class': 'form-control',})
		self.fields['asignado'].widget.attrs.update({'class': 'form-control',})
		
class CodgMatForm(forms.Form):

	class Meta:
		model = Materia
		exclude = []
		
	materia = forms.ModelMultipleChoiceField(Materia.objects.all(), widget=FilteredSelectMultiple("seleccionada", False, attrs={'rows':'10'}))

	def __init__(self, *args, **kwargs):
	    forms.ModelForm.__init__(self, *args, **kwargs)
	    self.fields['equipment'].queryset = Equipment.avail.all()

class CrearSecForm(forms.ModelForm):

	class Meta:
		model = PdoGradoSec
		fields = ('__all__')

	def __init__(self, *args, **kwargs):
		super(CrearSecForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})

class MatPenAlumnoForm(forms.ModelForm):

	class Meta:
		model = PdoGradoSec
		fields = ('__all__')	