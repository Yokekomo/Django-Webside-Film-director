from django.db import models
from django.utils.html import format_html


class Director(models.Model):
    nombre_dir = models.CharField(max_length=60)
    primer_apellido_dir = models.CharField(max_length=60)
    segundo_apellido_dir = models.CharField(max_length=60, null=True, blank=True)
    edad_dir = models.DateField(null=True, blank=True)
    fallecido_dir = models.DateField('Fallecido', null=True, blank=True)
    bio_dir = models.TextField(max_length=2000)
    avatar_dir = models.ImageField(upload_to='imagenes/', null=True, blank=True)

    def nombre(self):
        if self.segundo_apellido_dir is None:
            return '%s %s' % (self.nombre_dir, self.primer_apellido_dir)
        else:
            return '%s %s %s' % (self.nombre_dir, self.primer_apellido_dir, self.segundo_apellido_dir)

    def edad(self):
        if self.fallecido_dir is not None:
            return '%s, Fallecido %s' % (self.edad_dir, self.fallecido_dir)
        else:
            return '%s' % self.edad_dir

    def bio(self):
        return self.bio_dir[:165:] + '...'

    def foto(self):
        return format_html('<img src="{}" width=200 height=250 />', self.avatar_dir.url)

    def numero_pel(self):
        total_pel_dir = Peliculas.objects.filter(director_pel=self.id).count()
        return total_pel_dir

    def lista(self):
        lista = [self.nombre(), self.edad(), self.bio(), self.foto(), self.numero_pel()]
        return lista

    def __str__(self):
        return '%s %s %s' % (self.nombre_dir, self.primer_apellido_dir, self.segundo_apellido_dir)


class Meta(models.Model):
    verbose_name = "Item"
    verbose_name_plural = "Items"


class Genero(models.Model):
    genero = models.CharField(max_length=20, help_text="Genero")

    def __str__(self):
        return self.genero


class Peliculas(models.Model):
    nombre_pel = models.CharField(max_length=100)
    director_pel = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    genero_pel = models.ManyToManyField(Genero)
    premios_pel = models.CharField(max_length=200, help_text="Premios película")
    estreno_pel = models.IntegerField(null=True, blank=True)
    resumen_pel = models.TextField(max_length=2000, help_text="Resumen película")
    avatar_pel = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    trailer_pel = models.FileField(upload_to="videos/", max_length=100, null=True)

    def dame_genero_pel(self):
        total_gereros = Genero.objects.filter(id=self.id)
        return total_gereros

    def foto_pel_grande(self):
        return format_html('<img src="{}" width=320 height=470 />', self.avatar_pel.url)

    def foto_pel(self):
        return format_html('<img src="{}" width=200 height=250 />', self.avatar_pel.url)

    def trailer(self):
        return format_html('{}', self.trailer_pel.url)

    def bio_pel(self):
        return self.resumen_pel[:165:] + '...'

    def estreno(self):
        return 'Estreno: %s' % self.estreno_pel

    def __str__(self):
        return self.nombre_pel


class Frases(models.Model):
    frases_directores = models.CharField(max_length=100)

    def __str__(self):
        return self.frases_directores

