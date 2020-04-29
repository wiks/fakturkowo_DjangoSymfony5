# -*- coding: utf8 -*-

from django.urls import path
from items import views as items_views

urlpatterns = [
    path('', items_views.items_list, name='items_list'),  # lista towarów
]
