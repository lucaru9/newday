# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-25 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300, verbose_name='Nombre')),
                ('is_enabled', models.BooleanField(default=True, help_text='Habilitar o deshabilitar Categoria', verbose_name='Habilitado')),
                ('image', models.FileField(blank=True, null=True, upload_to='category/files')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300, verbose_name='Nombre')),
                ('address', models.CharField(max_length=500, verbose_name='Direcci\xf3n')),
                ('longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True, verbose_name='Longitud')),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True, verbose_name='Latitud')),
                ('is_enabled', models.BooleanField(default=True, help_text='Habilitar o deshabilitar lugar', verbose_name='Habilitado')),
                ('file_1', models.FileField(blank=True, null=True, upload_to='places/file')),
                ('file_2', models.FileField(blank=True, null=True, upload_to='places/file')),
                ('file_3', models.FileField(blank=True, null=True, upload_to='places/file')),
                ('description', models.TextField(blank=True, null=True)),
                ('score', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
    ]
