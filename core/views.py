from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
# Local imports
from .models import Inmueble, Favorito, Dispositivo, ImagenInmueble
from .filters import InmuebleFiltro

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'QuinesSomos.html')

def contacto(request):
    return render(request, 'contacto.html')

def inmuebles(request):
    inmuebles = Inmueble.objects.filter(status_de_venta='publicado')
    filtro = InmuebleFiltro(request.GET, queryset=inmuebles)

    # Paginador
    paginador = Paginator(filtro.qs, 6)
    page_number = request.GET.get('page')
    page_obj = paginador.get_page(page_number)

    elementos = len(list(filtro.qs))

    # favoritos


    contexto = {
        'page_ob':page_obj, 
        'filtro_inmueble':filtro, 
        'elementos':elementos, 
    }
    return render(request, 'inmuebles.html', contexto)

def single_inmueble(request, inmueble_id):
    inmueble = Inmueble.objects.get(id=inmueble_id)
    imagenes = ImagenInmueble.objects.filter(inmueble=inmueble)

    contexto = {'inmueble':inmueble, 'imagenes':imagenes}
    return render(request, 'singleInmueble.html', contexto)

def proyecto(request):
    return render(request, 'proyectos.html')

def proyecto_single(request):
    return render(request, 'proyectoSingle.html')

def updateFavoritos(request):

    response_json = request.body
    inmuebleId = None
    if response_json:
        data = json.loads(request.body)
        inmuebleId = data['id']
        inmueble = Inmueble.objects.get(id=int(inmuebleId))

        # cookies
        device = request.COOKIES['device'] 
        dipositivo, created = Dispositivo.objects.get_or_create(dispositivo_id=device)
        favorito, created = Favorito.objects.get_or_create(dispositivo=dipositivo, inmueble=inmueble)
        print('respuesta')
    
    ultimo_dispositivo = Dispositivo.objects.all().latest('id')
    favs = Favorito.objects.filter(dispositivo=ultimo_dispositivo) 

    contexto = {
        'id':inmuebleId,
        'favoritos':favs,
    }
    print(inmuebleId)
    return render(request, 'favoritos.html', contexto)

def eliminar_obj(request, id):
    fav_obj = get_object_or_404(Favorito, id=id)
    fav_obj.delete()

    return redirect(to='favoritos')