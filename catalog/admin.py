from django.contrib import admin
from django.utils.html import format_html

from .models import Director, Peliculas, Genero, Frases


class DirectorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_dir',
        'primer_apellido_dir',
        'segundo_apellido_dir',
        'edad_dir',
        'fallecido_dir',
        'bio_dir',
        'foto',
        'id',
    )

    search_fields = (
        'nombre_dir',
        'primer_apellido_dir',
        'segundo_apellido_dir',
    )

    def foto(self, obj):
        return format_html('<img src="{}" width=100 height=150 />', obj.avatar_dir.url)


class PeliculasAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_pel',
        'director_pel',
        'premios_pel',
        'estreno_pel',
        'bio_pel',
        'portada',
        'id'
    )

    def bio_pel(self, obj):
        return obj.resumen_pel[:165:] + '...'

    def portada(self, obj):
        return format_html('<img src="{}" width=100 height=150 />', obj.avatar_pel.url)

    search_fields = (
        'nombre_pel',
    )
    list_filter = (
        'director_pel',
    )


admin.site.register(Director, DirectorAdmin)
admin.site.register(Peliculas, PeliculasAdmin)
admin.site.register(Genero)
admin.site.register(Frases)
