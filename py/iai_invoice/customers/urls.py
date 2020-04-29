# -*- coding: utf8 -*-

from django.urls import path
from customers import views as customers_views
from customers import views_angular



urlpatterns = [
    path('', customers_views.customers_main, name='customers_main'),  # główna strona z listą klientów
    path('s/<int:customer_id>/', customers_views.customer_show, name='customer_show'),  # podgląd danych klienta
    path('e/', customers_views.customer_add_edit, name='customer_add'),  # dodanie danych klienta
    path('e/<int:customer_id>/', customers_views.customer_add_edit, name='customer_edit'),  # edycja danych klienta
    path('an/', views_angular.angular_url, name='angular_url'),  #

]
