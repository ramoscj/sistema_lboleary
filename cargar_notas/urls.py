from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from cargar_notas import views
from cargar_notas.views import DescargarXls


urlpatterns = [
	
	url(r'^descargar_xls/(?P<id_docente>[0-9]+)/(?P<id_periodo>[0-9]+)/$', views.DescargarXls, name='carga_xls'),
	url(r'^cargar_xls/$', views.CargarXlS, name='cargar_xls'),
	# url(r'^cargar_xls/insertar_notas/$', views.GuardarNotasLapso, name='insertar_notas'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)