# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django.db import models


# Third party apps imports


# Local imports


# Create your models here.
class School(models.Model):

    LEVEL_CHOICES = (
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria'),
    )

    break_time = models.PositiveSmallIntegerField('Minutos de recreo')
    classrooms = models.PositiveSmallIntegerField('Cantidad de aulas')
    hour_duration = models.PositiveSmallIntegerField(
        u'Minutos de duración de las horas académicas')
    hours = models.PositiveSmallIntegerField(u'Cantidad de horas académicas')
    level = models.CharField('Nivel', choices=LEVEL_CHOICES, max_length=10)
    name = models.CharField('Nombre', max_length=75)

    class Meta:
        verbose_name = 'Colegio'
        verbose_name_plural = 'Colegios'

    def __unicode__(self):
        return u'{}'.format(self.name)


class Classroom(models.Model):

    SECONDARY_CHOICES = (
        ('1', 'Primero'),
        ('2', 'Segundo'),
        ('3', 'Tercero'),
        ('4', 'Cuarto'),
        ('5', 'Quinto'), )

    PRIMARY_CHOICES = SECONDARY_CHOICES + (
        ('6', 'Sexto'), )

    grade = models.CharField('Grado', choices=PRIMARY_CHOICES, max_length=1)
    school = models.ForeignKey(School, verbose_name='Colegio')
    section = models.CharField('Seccion', max_length=1)

    class Meta:
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'
        unique_together = ['grade', 'school', 'section']

    def __unicode__(self):
        return u'{} {}'.format(self.grade, self.section)

    def save(self):
        self.section = self.section.upper()
        return super(Classroom, self).save()
