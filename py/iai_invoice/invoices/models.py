# -*- coding: utf8 -*-

from django.db import models
# from django.contrib.auth.models import User  # dla logowania i auth
from django.utils import timezone
from myfirm.models import FirmData
from items.models import Items, Vats


class Invoices(models.Model):
    """
    faktury
    """
    nr = models.CharField(default='', blank=True, null=True, max_length=50)  # numer faktury
    dt_created = models.DateField(default=None, blank=True, null=True)  # faktura z dnia
    dt_delivery = models.DateField(default=None, blank=True, null=True)  # data zakończenia dostawy lub wykonania usługi
    customer = models.ForeignKey(FirmData, on_delete=models.CASCADE)  # id klienta
    pay_form_id = models.IntegerField(default=None, blank=True, null=True)  # forma płatności, None = przelew
    dt_pait_to = models.DateField(default=None, blank=True, null=True)  # termin płatności
    person_auth_name = models.TextField(default=None, blank=True, null=True)  # osoba upoważniona do wystawienia faktury
    price_sum_netto = models.DecimalField(max_digits=10, decimal_places=2)  # wartość netto
    price_sum_brutto = models.DecimalField(max_digits=10, decimal_places=2)  # wartoć brutto
    paid_sum_brutto = models.DecimalField(max_digits=10, decimal_places=2)  # zapłacono
    dt_update = models.DateTimeField(default=timezone.now)


class InvoicesItems(models.Model):
    """
    towary dodane do faktury
    """
    invoice = models.ForeignKey(Invoices, on_delete=models.CASCADE)  # id faktury
    items = models.ForeignKey(Items, on_delete=models.CASCADE)  # id towaru na fakturze
    items_number = models.FloatField(default=None, blank=True, null=True)  # ilość

