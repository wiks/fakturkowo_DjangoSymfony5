# -*- coding: utf8 -*-

from django.urls import path
from invoices import views as invoices_views

urlpatterns = [
    path('', invoices_views.invoices_main, name='invoices_main'),  # główna strona zadania
    # lista faktur
    path('l', invoices_views.invoices_list, name='invoices_list'),
    # dodanie nowej faktury -wyszukanie firmy
    path('a/', invoices_views.invoice_add, name='invoice_add'),
    # dodanie nowej faktury do znanej firmy
    path('a/<int:customer_id>/', invoices_views.invoice_add, name='invoice_add'),
    # edycja
    path('e/<int:invoice_id>/', invoices_views.invoice_edit, name='invoice_edit'),

    # edycja, dodanie towaru - wybór towaru:
    path('ai/<int:invoice_id>/', invoices_views.invoice_add_item_choice, name='invoice_add_item_choice'),
    # edycja, dodanie towaru - określenie ilości towaru:
    path('ai/<int:invoice_id>/<int:item_id>/', invoices_views.invoice_add_item, name='invoice_add_item'),
    # usuwanie towaru
    path('di/<int:invoice_id>/<int:item_id>/<int:iid>/', invoices_views.invoice_del_item, name='invoice_del_item'),
    # podgląd finalny faktury
    path('s/<int:invoice_id>/', invoices_views.invoice_show, name='invoice_show'),
    # usuwanie faktury
    path('d/<int:invoice_id>/', invoices_views.invoice_delete, name='invoice_delete'),
]

