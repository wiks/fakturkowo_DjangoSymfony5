# -*- coding: utf8 -*-

from django.db import models
# from django.contrib.auth.models import User  # dla logowania i auth
from django.utils import timezone
# from items.models import Vats


class Vats(models.Model):
    """
    stawki VAT
    """
    percent = models.IntegerField()  #


class Jms(models.Model):
    """
    jednostki
    """
    name = models.TextField(default=None, blank=True, null=True)  # nazwa jednostki ('szt.', 'kg')


class Items(models.Model):
    """
    przedmioty/usługi
    """
    name = models.TextField(default=None, blank=True, null=True)  # nazwa towaru/usługi
    price_netto = models.DecimalField(max_digits=10, decimal_places=2)  # wartość netto
    vat = models.ForeignKey(Vats, on_delete=models.CASCADE)
    jm = models.ForeignKey(Jms, on_delete=models.CASCADE)

