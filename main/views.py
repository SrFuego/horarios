# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from django.views.generic.base import TemplateView


# Third party apps imports


# Local imports
from .forms import SchoolForm


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'


class SchoolFormView(FormView):

    form_class = SchoolForm
    template_name = 'main/school.html'

    def get_success_url(self):
        return reverse('main:index')

    def get_initial(self):
        initial = super(SchoolFormView, self).get_initial()
        print dir(self.request.GET)
        print dir(self.request.POST)
        initial['name'] = self.request
        return initial
