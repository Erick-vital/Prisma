from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros', views.about, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('inmuebles/', views.inmuebles, name='inmuebles'),
    path('proyectos', views.proyecto, name='proyectos'),
    path('proyecto', views.proyecto_single, name='proyecto'),
    path('inmueble/<inmueble_id>', views.single_inmueble, name='singleInmueble'),
    path('favoritos', views.updateFavoritos, name='favoritos'),
    path('eliminar/<int:id>', views.eliminar_obj, name='eliminar'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)