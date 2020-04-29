# -*- coding: utf8 -*-

from django.urls import path
from myfirm import views as myfirm_views

urlpatterns = [
    path('', myfirm_views.myfirm_main, name='myfirm_main'),  # główna strona danych własnych
    path('e/', myfirm_views.myfirm_edit, name='myfirm_edit'),  # edycja danych własnych
]
