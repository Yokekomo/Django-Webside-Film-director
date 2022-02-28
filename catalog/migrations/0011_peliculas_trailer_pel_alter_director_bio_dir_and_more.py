# Generated by Django 4.0.1 on 2022-02-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_meta_alter_director_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='peliculas',
            name='trailer_pel',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='director',
            name='bio_dir',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='premios_pel',
            field=models.CharField(help_text='Premios película', max_length=200),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='resumen_pel',
            field=models.TextField(help_text='Resumen película', max_length=2000),
        ),
    ]