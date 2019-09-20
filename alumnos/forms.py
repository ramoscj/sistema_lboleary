
from django import forms 
from alumnos.models import *
from django.contrib.auth.models import User
from django_superform import SuperModelForm, ModelFormField, ForeignKeyFormField

class AlumnoForm(forms.ModelForm):

	class Meta:
		model = Alumno
		fields = ('nombres', 'apellidos', 'nacionalidad', 'cedula', 'sexo', 'fchanac', 'lugarnac', 'correo',)
	
	def __init__(self, *args, **kwargs):
         super(AlumnoForm, self).__init__(*args, **kwargs)
         self.fields['nombres'].widget.attrs.update({'class': 'form-control has-feedback-left','placeholder': 'Nombres', 'style': 'text-transform:uppercase'})
         self.fields['apellidos'].widget.attrs.update({'class': 'form-control has-feedback-left','placeholder': 'Apellidos', 'style': 'text-transform:uppercase'})
         self.fields['nacionalidad'].widget.attrs.update({'class': 'form-control',})   
         self.fields['cedula'].widget.attrs.update({'class': 'form-control has-feedback-left','placeholder': 'Cedula'})
         self.fields['sexo'].widget.attrs.update({'class': 'form-control'}) 
         self.fields['fchanac'].widget.attrs.update({'class': 'date-picker form-control' ,'placeholder': 'dd/mm/aa', 'id': 'datepicker'})
         self.fields['lugarnac'].widget.attrs.update({'class': 'form-control',})
         self.fields['correo'].widget.attrs.update({'class': 'form-control has-feedback-left', 'placeholder': 'ejemplo@tudominio.com'})

class AlumnoDatosForm(forms.ModelForm):
	
	class Meta:
		model = DatosAlumno
		exclude = ['alumno', 'foto',]

	def __init__(self, *args, **kwargs):
		super(AlumnoDatosForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})
		self.fields['telefono'].widget.attrs.update({'class': 'form-control', 'data-inputmask' : '"mask" : "(9999) 999-9999"'})
		self.fields['peso'].widget.attrs.update({'class': 'form-control', 'data-inputmask' : '"mask" : "99,99"'})
		self.fields['estatura'].widget.attrs.update({'class': 'form-control', 'data-inputmask' : '"mask" : "9,99"'})
		self.fields['talla_p'].widget.attrs.update({'class': 'form-control', 'placeholder': '0'})
		self.fields['talla_z'].widget.attrs.update({'class': 'form-control', 'placeholder': '0'})
		
class AlumnRepreForm(forms.ModelForm):

	class Meta:
		model = RepresenAlumno
		exclude = ['alumno']

	def __init__(self, *args, **kwargs):
		super(AlumnRepreForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})
		self.fields['nombres'].widget.attrs.update({'class': 'form-control','placeholder': 'Nombres', 'required': 'required', 'style': 'text-transform:uppercase'})
		self.fields['apellidos'].widget.attrs.update({'class': 'form-control','placeholder': 'Apellidos', 'style': 'text-transform:uppercase'})
		self.fields['nacionalidad'].widget.attrs.update({'class': 'form-control',})
		self.fields['cedula'].widget.attrs.update({'class': 'form-control ','placeholder': 'Cedula'})
		self.fields['telefono'].widget.attrs.update({'class': 'form-control', 'data-inputmask' : '"mask" : "(9999) 999-9999"'})

class AlumnoSuperForm(SuperModelForm):

	datos = ModelFormField(AlumnoDatosForm)
	repres = ModelFormField(AlumnRepreForm)

	class Meta:
		model = Alumno
		fields = ('nombres', 'apellidos', 'nacionalidad', 'cedula', 'sexo', 'fchanac', 'lugarnac', 'correo',)
	
	def __init__(self, *args, **kwargs):
         super(AlumnoSuperForm, self).__init__(*args, **kwargs)
         self.fields['nombres'].widget.attrs.update({'class': 'form-control','placeholder': 'Nombres', 'required': 'required', 'style': 'text-transform:uppercase'})
         self.fields['apellidos'].widget.attrs.update({'class': 'form-control','placeholder': 'Apellidos', 'style': 'text-transform:uppercase'})
         self.fields['nacionalidad'].widget.attrs.update({'class': 'form-control',})   
         self.fields['cedula'].widget.attrs.update({'class': 'form-control ','placeholder': 'Cedula'})
         self.fields['sexo'].widget.attrs.update({'class': 'form-control'}) 
         self.fields['fchanac'].widget.attrs.update({'class': 'date-picker form-control' ,'placeholder': 'dd/mm/aa', 'id': 'datepicker'})
         self.fields['lugarnac'].widget.attrs.update({'class': 'form-control',})
         self.fields['correo'].widget.attrs.update({'class': 'form-control ', 'placeholder': 'ejemplo@tudominio.com'})