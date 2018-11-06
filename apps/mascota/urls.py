from django.conf.urls import url

from apps.mascota.views import index_mascota, mascota_view, mascota_list, mascota_edit, mascota_delete

urlpatterns = [
    url(r'^$', index_mascota, name='index_mascota'),
    url(r'^nuevo$', mascota_view, name='mascota_crear'),
    url(r'^listar$', mascota_list, name='mascota_listar'),
    url(r'^editar/(?P<id_mascota>\d+)$', mascota_edit, name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)$', mascota_delete, name='mascota_eliminar'),
]
