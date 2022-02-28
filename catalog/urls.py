

from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('buscar/', views.buscar_dir),
 path('ficha_dir/', views.ficha_dir),
 path('buscar/ficha_dir/', views.ficha_dir),
 path('ficha_pel/', views.ficha_pel),
 path('buscar/ficha_dir/ficha_pel/', views.ficha_pel),
]