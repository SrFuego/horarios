# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django.conf.urls import url


# Third party apps imports


# Local imports
from .views import IndexView, SchoolCreateView

# Create your tests here.


urlpatterns = [
    url(
        r'^$',
        IndexView.as_view(),
        name='index'
    ),
    url(
        r'^school/$',
        SchoolCreateView.as_view(),
        name='school'
    )
]
