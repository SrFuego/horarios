# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 04:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.PositiveSmallIntegerField(verbose_name='Cantidad de horas acad\xe9micas')),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('short_name', models.CharField(max_length=10, verbose_name=b'Nombre corto')),
            ],
            options={
                'verbose_name': '\xc1rea Acad\xe9mica',
                'verbose_name_plural': '\xc1reas Acad\xe9micas',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=50)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.Area')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('courses', models.ManyToManyField(to='academic.Course')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
            },
        ),
    ]