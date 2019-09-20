from django.conf import settings
from django import forms 
from .models import *
from django.contrib.auth.models import User


class CargarXLSForm(forms.Form):
 
    archivo = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(CargarXLSForm, self).__init__(*args, **kwargs)
        self.fields['archivo'].widget.attrs.update({'id': 'my_file_input',})

    def handle_uploaded_file(self, f):
        with open(('%s/%s') % (settings.MEDIA_ROOT, f.name), 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)