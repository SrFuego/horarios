# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django.conf.urls import url


# Third party apps imports


# Local imports
from .views import SchoolCreateView

# Create your tests here.


urlpatterns = [
    url(
        r'^school/$',
        SchoolCreateView.as_view(),
        name='create'
    )
]
