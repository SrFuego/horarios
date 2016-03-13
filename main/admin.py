# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import AcademicArea, Course, Teacher


# Register your models here.
@admin.register(AcademicArea)
class AcademicAreaAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'short_name',
        'hours',
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'short_name',
        'academic_area',
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    list_display = (
        '__unicode__',
        'get_courses',
    )
