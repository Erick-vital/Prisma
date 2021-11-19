import django_filters
from .models import Inmueble

class InmuebleFiltro(django_filters.FilterSet):
    precio__gt = django_filters.NumberFilter(field_name='precio', lookup_expr='gt')
    precio__lt = django_filters.NumberFilter(field_name='precio', lookup_expr='lt')
    metros_cuadrados__gt = django_filters.NumberFilter(field_name='metros_cuadrados', lookup_expr='gt')
    metros_cuadrados__lt = django_filters.NumberFilter(field_name='metros_cuadrados', lookup_expr='lt')
    class Meta:
        model = Inmueble
        fields = '__all__'
        exclude = ['precio', 'descripcion', 'imagen', 'metros_cuadrados']