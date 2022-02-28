# Generated by Django 4.0.1 on 2022-02-20 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_dir', models.CharField(max_length=60)),
                ('primer_apellido_dir', models.CharField(max_length=60)),
                ('segundo_apellido_dir', models.CharField(max_length=60)),
                ('edad_dir', models.DateField(blank=True, null=True)),
                ('fallecido_dir', models.DateField(blank=True, null=True, verbose_name='Fallecido')),
                ('bio_dir', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(help_text='Genero', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pel', models.CharField(max_length=100)),
                ('premios_pel', models.CharField(help_text='Premios película', max_length=60)),
                ('estreno_pel', models.DateField(blank=True, null=True)),
                ('resumen_pel', models.TextField(help_text='Resumen película', max_length=200)),
                ('director_pel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.director')),
                ('genero_pel', models.ManyToManyField(to='catalog.Genero')),
            ],
        ),
    ]