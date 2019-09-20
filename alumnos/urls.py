from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from alumnos import views

urlpatterns = [
	# Urls de Estudiantes
	url(r'^$', views.AgregarAlumno, name='inicio'),
	url(r'^datos_extra/(?P<alumnopk>[0-9]+)/$', views.DatosExtrasAlumno, name='datos_alumno'),
	url(r'^datos_extra/(?P<alumnopk>[0-9]+)/editar_datos/$', views.EditDatosAlumno, name='editar_datos'),
	url(r'^lista_alumnos/$', views.ListaAlumnos, name='lista_alumnos'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)