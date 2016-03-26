# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django import forms


# Third party apps imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


# Local imports
from schools.models import School


# Create your forms here.
class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = (
            'name', 'level', 'classrooms', 'hours', 'hour_duration',
            'break_time', )

    def __init__(self, *args, **kwargs):
        super(SchoolForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Enviar'))

    def clean(self):
        return self.cleaned_data
