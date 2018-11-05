from django.conf.urls import url, include

from apps.adopcion.views import index, adopcion_view

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^nuevo$', adopcion_view, name='formulario'),
]