from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.adopcion.views import index, adopcion_view

urlpatterns = [
	url(r'^$', login_required(index), name='index'),
	url(r'^crear$', login_required(adopcion_view), name='persona_nueva'),
]