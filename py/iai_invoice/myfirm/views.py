# -*- coding: utf8 -*-

# import os
# import imghdr
import json
# import time
import logging
# from PIL import Image, ImageDraw  # pip install Pillow  # Successfully installed Pillow-6.1.0
# from django.utils import timezone
from myfirm.models import FirmData
from django.shortcuts import render
from django.shortcuts import redirect
from myfirm.utils import validation_firm
from myfirm.utils import myfirm_parser
from myfirm.utils import breadcrumbsutil
logger = logging.getLogger('debug')


def index(request):
    """
    opis zadania do wykonania
    :param request:
    :return:
    """
    response = None
    web_context = {}

    if not response:
        response = render(request, 'index.html', web_context)
    return response


def myfirm_main(request):
    """
    zwraca widok z podglądem danych własnej firmy
    :param request:
    :return:
    """
    response = None
    web_context = {}
    bc = breadcrumbsutil.Breadcrumbs()
    breadcrumbs = bc.myfirm()
    web_context['breadcrumbs'] = breadcrumbs
    if request.method == 'POST':
        action = request.POST.get('action')
        logger.debug('action... --> %s', action)
        if action == 'Cancel':
            response = redirect('invoices_main')
        if action == 'create_edit':
            response = redirect('myfirm_edit')

    firm_data_obj = FirmData.objects.filter(id=1).first()
    web_context['firm_data_obj'] = firm_data_obj
    if firm_data_obj:
        ddp = myfirm_parser.MyFirmParser()
        web_context = ddp.update_webkontext(web_context, firm_data_obj)
        logger.debug('web_context %s', web_context)
    if not response:
        # response = render(request, 'customers/firm_show_mini.html', web_context)
        response = render(request, 'myfirm/myfirm_show.html', web_context)
    return response


def myfirm_edit(request):
    """
    edycja danych własnych
    :param request:
    :return:
    """
    response = None
    web_context = {}
    bc = breadcrumbsutil.Breadcrumbs()
    breadcrumbs = bc.myfirm()
    web_context['breadcrumbs'] = breadcrumbs

    firm_data_obj = FirmData.objects.filter(id=1).first()
    if not firm_data_obj:
        firm_data_obj = FirmData()
        firm_data_obj.id=1
        firm_data_obj.save()
    ddp = myfirm_parser.MyFirmParser()

    # z obiektu na stronę:
    web_context = ddp.update_webkontext(web_context, firm_data_obj)

    # firmName, \
    #     address_list, \
    #     mInputEmail, \
    #     firmNip, \
    #     firmRegon, \
    #     firmPesel, \
    #     firm_account_list = ddp.myfirm_pickup(firm_data_obj)

    errors_message_list = []
    errors_message_redclass_list = []
    if request.method == 'POST':
        action = request.POST.get('action')
        logger.debug('action... --> %s', action)
        if action == 'Cancel':
            response = redirect('invoices_main')
        if action == 'OK':
            firmName, \
                address_list, \
                mInputEmail, \
                firmNip, \
                firmRegon, \
                firmPesel, \
                firm_account_list = ddp.data_firm_from_postrequest(request)

            # uzupełniam kontext, gdyby nie pyknęło...
            web_context = ddp.from_request_to_webcontext_firm(web_context,
                                                         firmName,
                                                         address_list,
                                                         mInputEmail,
                                                         firmNip,
                                                         firmRegon,
                                                         firmPesel,
                                                         firm_account_list)

            mv = validation_firm.ValidationFirm()
            fname, \
                address_json, \
                email, \
                nip, \
                regon, \
                pesel, \
                bank_json, \
                errors_message_list, \
                errors_message_redclass_list \
                    = mv.validate_complet_firm_data(firmName,
                                                    address_list[0], address_list[1], address_list[2], address_list[3], address_list[4],
                                                    mInputEmail,
                                                    firmNip,
                                                    firmRegon,
                                                    firmPesel,
                                                    firm_account_list[0], firm_account_list[1])
            logger.debug('%s', errors_message_list)
            logger.debug('%s', errors_message_redclass_list)
            logger.debug('%s %s %s %s %s %s %s',
                         fname, address_json, email, nip, regon, pesel, bank_json)
            # DEBUG 2020-04-23 13:35:16,461 views
            # qwe
            # ["qweqwe", "qweqweqwe", "qweqweqweqwe"]
            # ert@wp.pl
            # 573-214-78-63
            # 234567890
            # 71050103357
            # ["75 1020 4870 0000 5602 0076 5859", "mBank"]
            if not errors_message_redclass_list:
                firm_data_obj.fname = fname
                firm_data_obj.address_json = address_json
                firm_data_obj.email = email
                firm_data_obj.nip = nip
                firm_data_obj.regon = regon
                firm_data_obj.pesel = pesel
                firm_data_obj.bank_account = bank_json
                firm_data_obj.save()
                response = redirect('myfirm_main')

    web_context['errors_message_list'] = errors_message_list
    web_context['errors_message_redclass_list'] = errors_message_redclass_list

    logger.debug('web_context %s', web_context)
    if not response:
        response = render(request, 'myfirm/myfirm_edit.html', web_context)
    return response
