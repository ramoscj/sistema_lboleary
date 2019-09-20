from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy


urlpatterns = [

	url(r'^$', login, {'template_name': 'ingresar.html'}, name='misitio_ingresar'),
    url(r'^logout/$', logout, {'next_page': 'misitio_ingresar'}, name='misitio_salir'),

]