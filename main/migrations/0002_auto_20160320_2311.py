# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 04:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='academic_area',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='courses',
        ),
        migrations.DeleteModel(
            name='AcademicArea',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
