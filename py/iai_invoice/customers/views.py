# -*- coding: utf8 -*-

import json
from django.http import JsonResponse
import logging
from myfirm.models import FirmData
from items.models import Items
from django.shortcuts import render
from django.shortcuts import redirect
from myfirm.utils import validation_firm
from myfirm.utils import myfirm_parser
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from myfirm.utils import breadcrumbsutil
logger = logging.getLogger('debug')


def customers_main(request):
    """
    lista klientów
    :param request:
    :return:
    """
    response = None
    web_context = {}
    bc = breadcrumbsutil.Breadcrumbs()
    breadcrumbs = bc.customers()
    web_context['breadcrumbs'] = breadcrumbs

    customers_objs = FirmData.objects.filter(id__gt=1,
                                             fname__isnull=False).values('id', 'fname', 'icon')
    # --------- paginator -----------------------------
    page = request.GET.get('page', 1)
    max_items_per_page = 2
    paginator = Paginator(customers_objs, max_items_per_page)
    try:
        range_answers_with_opinion = paginator.page(page)
    except PageNotAnInteger:
        range_answers_with_opinion = paginator.page(1)
    except EmptyPage:
        range_answers_with_opinion = paginator.page(paginator.num_pages)
    web_context['corected_pagination'] = range_answers_with_opinion
    # web_context['customers_corected_length'] = len(customers_objs)
    web_context['paginator'] = paginator
    # --------- paginator -----------------------------
    web_context['customers_objs'] = customers_objs
    if not response:
        response = render(request, 'customers/customers_main.html', web_context)
    return response


def customer_show(request, customer_id):
    """

    :param response:
    :param customer_id:
    :return:
    """
    response = None
    web_context = {}
    bc = breadcrumbsutil.Breadcrumbs()
    breadcrumbs = bc.customer_one()
    web_context['breadcrumbs'] = breadcrumbs

    ddp = myfirm_parser.MyFirmParser()
    customer_obj = None
    if customer_id and customer_id > 1:
        customer_obj = FirmData.objects.filter(id=customer_id).first()
    if not customer_obj:
        response = redirect('customers_main')

    if request.method == 'POST':
        action = request.POST.get('action')
        logger.debug('action... --> %s', action)
        if action == 'Cancel':
            response = redirect('invoices_main')
        if action == 'create_edit':
            response = redirect('customer_edit', customer_id)

    web_context['firm_data_obj'] = customer_obj
    web_context = ddp.update_webkontext(web_context, customer_obj)

    logger.debug('web_context %s', web_context)
    if not response:
        response = render(request, 'customers/customer_show.html', web_context)
    return response


def customer_add_edit(request, customer_id=None):
    """

    :param request:
    :param customer_id:
    :return:
    """
    response = None
    web_context = {}
    bc = breadcrumbsutil.Breadcrumbs()
    breadcrumbs = bc.customer_one('nowy klient')
    web_context['breadcrumbs'] = breadcrumbs

    ddp = myfirm_parser.MyFirmParser()
    customer_obj = None
    if customer_id and customer_id > 1:
        customer_obj = FirmData.objects.filter(id=customer_id).first()
    if not customer_obj:
        customer_obj = FirmData()

    # web_context['customer_obj'] = customer_obj
    # z obiektu na stronę:
    web_context = ddp.update_webkontext(web_context, customer_obj)

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

            if not errors_message_redclass_list:
                customer_obj.fname = fname
                customer_obj.address_json = address_json
                customer_obj.email = email
                customer_obj.nip = nip
                customer_obj.regon = regon
                customer_obj.pesel = pesel
                customer_obj.bank_account = bank_json
                customer_obj.save()
                response = redirect('customer_show', customer_obj.id)

            web_context['errors_message_list'] = errors_message_list
            web_context['errors_message_redclass_list'] = errors_message_redclass_list

    # # z obiektu na stronę:
    # web_context = ddp.update_webkontext(web_context, customer_obj)

    logger.debug('web_context %s', web_context)
    if not response:
        response = render(request, 'customers/customer_edit.html', web_context)
    return response


