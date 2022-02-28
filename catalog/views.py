from random import randint

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Peliculas, Director, Frases


def dame_random():

    numero = Frases.objects.all().count()
    numero_random = randint(1, numero)
    dame_frase = Frases.objects.filter(id=numero_random)
    return dame_frase


def dame_director(nombre):

    director = Director.objects.filter(nombre_dir__icontains=nombre)
    return director


def index(request):

    los_directores = Director.objects.all().order_by('nombre_dir')

    paginator = Paginator(los_directores, 10)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'catalog/index.html', {
        'meta_description': '',
        'meta_keywords': '',
        'items': items,
        'lista_frases': dame_random(),
    })


def buscar_dir(request):

    if request.GET['buscar_dir']:
        busqueda = request.GET['buscar_dir'].capitalize()

        if len(busqueda) >= 30:
            mensaje = 'Ha introducido demasiados caracteres'

        else:
            return render(request, 'catalog/directores.html', {
                'director': dame_director(busqueda),
                'query': busqueda,
                'lista_frases': dame_random(),
            })
    else:
        mensaje = 'No has introducido ningún termino'

    return render(request, 'catalog/directores.html', {
        'query': mensaje,
        'lista_frases': dame_random(),
    })


def ficha_dir(request):

    page = request.GET.get('page')
    director = Director.objects.filter(id=page)
    total_pel_dir = Peliculas.objects.filter(director_pel=page)

    return render(request, 'catalog/ficha_dir.html', {
        'total_pel_dir': total_pel_dir,
        'page': page,
        'director': director,
        'lista_frases': dame_random(),
    })


def ficha_pel(request):

    page = request.GET.get('page')
    pelicula = Peliculas.objects.filter(id=page)

    return render(request, 'catalog/ficha_pel.html', {

        'page': page,
        'pelicula': pelicula,
        'lista_frases': dame_random(),
    })