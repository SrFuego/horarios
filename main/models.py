# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django.db import models


# Third party apps imports


# Local imports


# Create your models here.
class AcademicArea(models.Model):

    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)
    hours = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = u'Área Académica'
        verbose_name_plural = u'Áreas Académicas'

    def __unicode__(self):
        return u'{}'.format(self.name)


class Course(models.Model):

    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)
    academic_area = models.ForeignKey(AcademicArea)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __unicode__(self):
        return u'{}'.format(self.name)


class Teacher(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __unicode__(self):
        return u'{}, {}'.format(self.last_name, self.first_name)

    def get_courses(self):
        return ', '.join([course.name for course in self.courses.all()])
    get_courses.short_description = 'Cursos'
