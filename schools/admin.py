# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import School


# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'level', 'classrooms', 'hours', 'hour_duration',
        'break_time', )
