from django.conf import settings
from django import forms 
from .models import *
from django.contrib.auth.models import User

class MaestroForm(forms.ModelForm):

	class Meta:
		model = Maestro 
		exclude = ['foto']

	def __init__(self, *args, **kwargs):
		super(MaestroForm, self).__init__(*args, **kwargs)
		self.fields['nombres'].widget.attrs.update({'class': 'form-control has-feedback-left','placeholder': 'Nombres', 'style': 'text-transform:uppercase'})
		self.fields['apellidos'].widget.attrs.update({'class': 'form-control has-feedback-left','placeholder': 'Apellidos', 'style': 'text-transform:uppercase'})
		self.fields['nacionalidad'].widget.attrs.update({'class': 'form-control',})
		self.fields['cedula'].widget.attrs.update({'class': 'form-control has-feedback-left','placeholder': 'Cedula'})
		self.fields['sexo'].widget.attrs.update({'class': 'form-control'}) 
		self.fields['fchanac'].widget.attrs.update({'class': 'date-picker form-control' ,'placeholder': 'dd/mm/aa', 'id': 'datepicker'})
		self.fields['correo'].widget.attrs.update({'class': 'form-control has-feedback-left', 'placeholder': 'ejemplo@tudominio.com'})