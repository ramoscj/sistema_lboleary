from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from docentes import views

urlpatterns = [
	
	url(r'^registro_docente/$', views.RegistrarMaestro, name='registro_docente'),
	url(r'^lista_docentes/$', views.ListaMaestros, name='lista_docentes'),
	url(r'^lista_docentes/periodo/(?P<id_docente>[0-9]+)/$', views.PeriodoMaterias, name='lista_periodo'),
	url(r'^lista_docentes/periodo/(?P<id_docente>[0-9]+)/materias/$', views.MateriasDocente, name='lista_periodo_materias'),
	url(r'^lista_docentes/(?P<id_docente>[0-9]+)/actualizar$', views.EditarMaestro, name='actualizar_docente'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)