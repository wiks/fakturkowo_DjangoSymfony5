# -*- coding: utf8 -*-

from django.db import models
# from django.contrib.auth.models import User  # dla logowania i auth
from django.utils import timezone


class FirmData(models.Model):
    """
    firmę mam jedną,
    ale założę tutaj ogólny model, który NIE uniemożliwi mi utworzeniu kilku wystawców faktur

    qwe
    ["qweqwe", "qweqweqwe", "qweqweqweqwe"]
    ert@wp.pl
    573-214-78-63
    234567890
    71050103357
    ["75 1020 4870 0000 5602 0076 5859", "mBank"]

    """
    fname = models.TextField()  # nazwa 'techniczna'
    address_json = models.TextField(default=None, blank=True, null=True)  # json, umożliwi mi dodanie wielu linii
    email = models.EmailField(default=None, blank=True, null=True)  # mogłoby być powyżej, ale zrobię osobno
    nip = models.TextField(default=None, blank=True, null=True)
    regon = models.TextField(default=None, blank=True, null=True)
    pesel = models.TextField(default=None, blank=True, null=True)
    bank_account = models.TextField(default=None, blank=True, null=True)  # json, nazwa i numer konta
    # to opcjonalnie, jak zdążę dodać drop-zone to użyje, jak nie to nie
    icon = models.TextField(default=None, blank=True, null=True)  # jeśli tylko zapragnę
    dt_update = models.DateTimeField(default=timezone.now)


