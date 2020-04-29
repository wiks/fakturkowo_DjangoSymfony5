# -*- coding: utf8 -*-

import logging
from django.utils import timezone
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from invoices.models import Invoices
from invoices.models import InvoicesItems
# from items.models import Vats
from items.models import Items
from myfirm.models import FirmData
# from myfirm.utils import myfirm_parser
from myfirm.utils import breadcrumbsutil
from invoices.utils import invoice_parser
from invoices.utils import invoices_common
from iai_invoice.utils import validation_invoice
import math

logger = logging.getLogger('debug')


def invoices_main(request):
    """
    widok menu głównego
    :param request:
    :return:
    """
    response = None
    web_context = {}
    bc = breadcrumbsutil.Breadcrumbs()
    breadcrumbs = bc.home()
    web_context['breadcrumbs'] = breadcrumbs

    if not response:
        response = render(request, 'invoices/invoices_main.html', web_context)
    return response


def invoices_list(request):
    """
    widok listy faktur
    :param request:
    :return:
    """
    response = None
    web_context = {}
    bc = breadcrumbsutil.Breadcrumbs()
    breadcrumbs = bc.invoices()
    web_context['breadcrumbs'] = breadcrumbs
    invoices_objs = Invoices.objects.all()
    logger.debug('invoices_objs: %s', invoices_objs)
    # --------- paginator -----------------------------
    page = request.GET.get('page', 1)
    max_items_per_page = 2
    paginator = Paginator(invoices_objs, max_items_per_page)
    try:
        range_answers_with_opinion = paginator.page(page)
    except PageNotAnInteger:
        range_answers_with_opinion = paginator.page(1)
    except EmptyPage:
        range_answers_with_opinion = paginator.page(paginator.num_pages)
    web_context['corected_pagination'] = range_answers_with_opinion
    web_context['paginator'] = paginator
    # --------- paginator -----------------------------

    web_context['invoices_objs'] = invoices_objs
    if not response:
        response = render(request, 'invoices/invoices_list.html', web_context)
    return response


def invoice_add(request, customer_id=None):
    """
    widok dodanie nowej faktury - wybór klienta
    :param request:
    :param customer_id:
    :return:
    """
    # response = None
    web_context = {}
    bc = breadcrumbsutil.Breadcrumbs()
    breadcrumbs = bc.invoice_one('nowa faktura')
    web_context['breadcrumbs'] = breadcrumbs

    customer = None
    if customer_id:
        customer = FirmData.objects.filter(id=customer_id).first()
    if customer:
        icom = invoices_common.InvoicesCommon()
        invoice_obj = icom.create_empty_invoice(customer.id)
        return redirect('invoice_edit', invoice_obj.id)  # przechodzę do edycji już istniejącej faktury (ten sam widok)

    # wyszukaj firmę, bo jeszcze nie jest ustalona
    return render(request, 'invoices/invoice_add.html', web_context)


def invoice_edit(request, invoice_id=None):
    """

    :param request:
    :return:
    """
    # response = None
    web_context = {}
    bc = breadcrumbsutil.Breadcrumbs()
    breadcrumbs = bc.invoice_one()
    web_context['breadcrumbs'] = breadcrumbs

    invoice_obj = None
    if invoice_id:
        invoice_obj = Invoices.objects.filter(id=invoice_id).first()
    if not invoice_obj:
        return redirect('invoices_list')

    # to będzie potrzebne przy dodawaniu towaru
    web_context['invoice'] = invoice_obj

    # sprzedawca stały - z poz.1, kupujący z customer_id - albo z PATH albo z obiektu faktury
    # customer = FirmData.objects.filter(id=invoice_obj.customer.id).first()
    # seller = FirmData.objects.filter(id=1).first()
    # web_context['customer'] = invoice_obj.customer
    # web_context['seller'] = seller
    # dt_now = datetime.now()
    # web_context['dt_created'] = dt_now.strftime("%Y-%m-%d")
    # web_context['dt_pait_to'] = (dt_now + timezone.timedelta(days=30)).strftime("%Y-%m-%d")
    # web_context['dt_delivery'] = (dt_now + timezone.timedelta(days=30)).strftime("%Y-%m-%d")

    inp = invoice_parser.InvoiceParser()

    web_context['fNr'],\
        web_context['customer'], \
        web_context['seller'], \
        invoices_items_richer, \
        web_context['vat_sum'], \
        web_context['price_sum_netto'], \
        web_context['price_sum_brutto'], \
        web_context['paid_form'], \
        web_context['person_auth_name'], \
        web_context['dt_created'], \
        web_context['dt_pait_to'], \
        web_context['dt_delivery'], \
        web_context['paid_sum_brutto'] = inp.invoice_pickup(invoice_obj)
    web_context['invoices_items_richer'] = invoices_items_richer

    if request.method == 'POST':
        action = request.POST.get('action')
        logger.debug('action... --> %s', action)
        if action == 'Cancel':
            return redirect('invoices_main')
        if action == 'delete':
            if invoice_obj and invoice_obj.id:
                return redirect('invoice_delete', invoice_obj.id)
            else:
                return redirect('invoices_list')
        if action == 'add_item':
            logger.debug('życzenie dodania pozycji do faktury')
            return redirect('invoice_add_item', invoice_obj.id, 0)
        if action == 'OK':
            logger.debug('%s', request.POST)

            fNr, \
                person_auth_name, \
                dt_created, \
                dt_pait_to, \
                dt_delivery,\
                paid_sum_brutto, \
                pay_form_id = inp.data_invoice_from_postrequest(request)

            # uzupełniam kontext, gdyby nie pyknęło...
            web_context = inp.from_request_to_webcontext_invoice(web_context,
                                                                 fNr,
                                                                 invoice_obj.customer,
                                                                 web_context['seller'],
                                                                 person_auth_name,
                                                                 dt_created,
                                                                 dt_pait_to,
                                                                 dt_delivery,
                                                                 paid_sum_brutto)

            mv = validation_invoice.ValidationInvoice()
            fv_fNr, \
                fv_person_auth_name, \
                fv_dt_created, \
                fv_dt_pait_to, \
                fv_dt_delivery, \
                errors_message_list, \
                errors_message_redclass_list = mv.validate_complet_invoice_data(invoice_obj,
                                                                                fNr,
                                                                                person_auth_name,
                                                                                dt_created,
                                                                                dt_pait_to,
                                                                                dt_delivery
                                                                                )
            if not errors_message_redclass_list:

                invoice_obj.nr = fv_fNr
                if fv_dt_created:
                    invoice_obj.dt_created = datetime.strptime(fv_dt_created, '%Y-%m-%d')
                if fv_dt_delivery:
                    invoice_obj.dt_delivery = datetime.strptime(fv_dt_delivery, '%Y-%m-%d')
                # invoice_obj.customer = customer
                if fv_dt_pait_to:
                    invoice_obj.dt_pait_to = datetime.strptime(fv_dt_pait_to, '%Y-%m-%d')
                invoice_obj.person_auth_name = fv_person_auth_name

                invoice_obj.price_sum_brutto = 0
                invoice_obj.price_sum_netto = 0
                # invoice_obj.paid_sum_brutto = 0

                invoice_obj.paid_sum_brutto = paid_sum_brutto
                invoice_obj.pay_form_id = pay_form_id  # None to przelew

                invoice_obj.save()

                return redirect('invoice_edit', invoice_obj.id)  # przechodzę do edycji już istniejącej faktury (ten sam widok)

            web_context['errors_message_list'] = errors_message_list
            web_context['errors_message_redclass_list'] = errors_message_redclass_list

    logger.debug('web_context: %s', web_context)

    # if not response:
    response = render(request, 'invoices/invoice_edit.html', web_context)
    return response


def invoice_add_item_choice(request, invoice_id=None):
    """
    widok wybrania towaru do dodania
    :param request:
    :return:
    """
    response = None
    errors_message_list = []
    web_context = {}
    bc = breadcrumbsutil.Breadcrumbs()
    breadcrumbs = bc.invoice_one()
    web_context['breadcrumbs'] = breadcrumbs

    invoice_obj = None
    if invoice_id:
        invoice_obj = Invoices.objects.filter(id=invoice_id).first()
    if not invoice_obj:
        return redirect('invoices_list')

    # to będzie potrzebne przy dodawaniu towaru
    web_context['invoice'] = invoice_obj

    # sprzedawca stały - z poz.1, kupujący z customer_id - albo z PATH albo z obiektu faktury
    # customer = FirmData.objects.filter(id=invoice_obj.customer.id).first()
    # seller = FirmData.objects.filter(id=1).first()
    # web_context['customer'] = invoice_obj.customer
    # web_context['seller'] = seller
    # dt_now = datetime.now()
    # web_context['dt_created'] = dt_now.strftime("%Y-%m-%d")
    # web_context['dt_pait_to'] = (dt_now + timezone.timedelta(days=30)).strftime("%Y-%m-%d")
    # web_context['dt_delivery'] = (dt_now + timezone.timedelta(days=30)).strftime("%Y-%m-%d")

    inp = invoice_parser.InvoiceParser()

    web_context['fNr'],\
        web_context['customer'], \
        web_context['seller'], \
        invoices_items_richer, \
        web_context['vat_sum'], \
        web_context['price_sum_netto'], \
        web_context['price_sum_brutto'], \
        web_context['paid_form'], \
        web_context['person_auth_name'], \
        web_context['dt_created'], \
        web_context['dt_pait_to'], \
        web_context['dt_delivery'], \
        web_context['paid_sum_brutto'] = inp.invoice_pickup(invoice_obj)
    web_context['invoices_items_richer'] = invoices_items_richer

    logger.debug('nie mam określonego towaru, więc wybór towaru teraz')
    logger.debug('web_context: %s', web_context)
    return render(request, 'invoices/invoice_add_item_choice.html', web_context)


def invoice_add_item(request, invoice_id=None, item_id=None):
    """

    :param request:
    :return:
    """
    response = None
    errors_message_list = []
    web_context = {}
    bc = breadcrumbsutil.Breadcrumbs()
    breadcrumbs = bc.invoice_one()
    web_context['breadcrumbs'] = breadcrumbs

    invoice_obj = None
    if invoice_id:
        invoice_obj = Invoices.objects.filter(id=invoice_id).first()
    if not invoice_obj:
        return redirect('invoice_edit')

    # to będzie potrzebne przy dodawaniu towaru
    web_context['invoice'] = invoice_obj

    inp = invoice_parser.InvoiceParser()

    web_context['fNr'],\
        web_context['customer'], \
        web_context['seller'], \
        invoices_items_richer, \
        web_context['vat_sum'], \
        web_context['price_sum_netto'], \
        web_context['price_sum_brutto'], \
        web_context['paid_form'], \
        web_context['person_auth_name'], \
        web_context['dt_created'], \
        web_context['dt_pait_to'], \
        web_context['dt_delivery'], \
        web_context['paid_sum_brutto'] = inp.invoice_pickup(invoice_obj)
    web_context['invoices_items_richer'] = invoices_items_richer

    item_obj = None
    if item_id:
        # logger.debug('dodaję przedmiot do faktury: ID: %s', item_id)
        item_obj = Items.objects.filter(id=item_id).first()

    if not item_obj:
        logger.debug('nie mam określonego towaru, więc wybór towaru teraz')
        # return redirect('invoice_edit')
        return render(request, 'invoices/invoice_add_item_choice.html', web_context)

    web_context['item'] = item_obj

    # icom = invoices_common.InvoicesCommon()
    # response = icom.edit_item_add_part(request, web_context, invoice_obj, item_obj)
    # if response:
    #     return response

    if request.method == 'POST':
        action = request.POST.get('action')
        logger.debug('action... --> %s', action)
        if action == 'Cancel':
            response = redirect('invoices_main')
        if action == 'OK':
            logger.debug('%s', request.POST)

            item_amount = request.POST.get('item_amount', None)

            invoices_items_obj, \
                errors_message_list = inp.add_item_to_invoice(invoice_obj,
                                                              item_obj,
                                                              item_amount,
                                                              errors_message_list)
            if invoices_items_obj:
                logger.debug('dodany/updatowany przedmiot do faktury %s', invoices_items_obj)
                return redirect('invoice_edit', invoice_obj.id)
            web_context['errors_message_list'] = errors_message_list

    logger.debug('web_context: %s', web_context)
    if not response:
        response = render(request, 'invoices/invoice_edit_add_item.html', web_context)
        # response = render(request, 'invoices/invoice_add_item.html', web_context)
    return response


def invoice_del_item(request, invoice_id, item_id, iid):
    """
    usuwanie jednej pozycji z faktury
    :param request:
    :param invoice_id: ID faktury
    :param item_id: ID pozycji fakturowej
    :param iid: ID towaru na liście towarów
    :return:
    """
    invoice_obj = Invoices.objects.filter(id=invoice_id).first()
    if invoice_obj:
        item_obj = Items.objects.filter(id=iid).first()
        if item_obj:
            # icom = invoices_common.InvoicesCommon()
            logger.debug('usuwanie towaru z faktury')
            invoices_items_obj = InvoicesItems.objects.filter(invoice=invoice_obj,
                                                              items=item_obj,
                                                              id=item_id,
                                                              ).first()
            if invoices_items_obj:
                invoices_items_obj.delete()
    return redirect('invoice_edit', invoice_id)


def invoice_show(request, invoice_id):
    """

    :param request:
    :return:
    """
    response = None
    web_context = {}
    # bc = breadcrumbsutil.Breadcrumbs()
    # breadcrumbs = bc.invoice_one()
    # web_context['breadcrumbs'] = breadcrumbs

    invoice_obj = Invoices.objects.filter(id=invoice_id).first()
    if not invoice_obj:
        return redirect('invoices_list')
    if request.method == 'POST':
        action = request.POST.get('action')
        logger.debug('action... --> %s', action)
        if action == 'Cancel':
            return redirect('invoices_list')
        if action == 'edit':
            response = redirect('invoice_edit', invoice_obj.id)
        if action == 'delete':
            response = redirect('invoice_delete', invoice_obj.id)
        if action == 'OK':
            # todo drukuj
            # window.print();
            pass

    # breadcrumbs = []
    # breadcrumbs.append({'name': 'Home', 'url': None})
    # breadcrumbs.append({'name': 'lista faktur', 'url': 'invoices_list'})
    # breadcrumbs.append({'name': 'faktura ' + str(invoice_obj.nr), 'url': None})
    # web_context['breadcrumbs'] = breadcrumbs

    icom = invoices_common.InvoicesCommon()
    web_context = icom.common_invoice_middle_show(web_context, invoice_obj)
    # logger.debug('web_context: %s', web_context)
    if not response:
        response = render(request, 'invoices/invoice_show.html', web_context)
    return response


def invoice_delete(request, invoice_id):
    """

    :param request:
    :return:
    """
    response = None
    web_context = {}
    bc = breadcrumbsutil.Breadcrumbs()
    breadcrumbs = bc.invoice_one()
    web_context['breadcrumbs'] = breadcrumbs

    invoice_obj = Invoices.objects.filter(id=invoice_id).first()
    if not invoice_obj:
        return redirect('invoices_list')
    if request.method == 'POST':
        action = request.POST.get('action')
        # logger.debug('action... --> %s', action)
        if action == 'Cancel':
            return redirect('invoices_list')
        if action == 'delete':
            invoice_obj.delete()
            return redirect('invoices_list')
    icom = invoices_common.InvoicesCommon()
    web_context = icom.common_invoice_middle_show(web_context, invoice_obj)
    if not response:
        response = render(request, 'invoices/invoice_delete.html', web_context)
    return response



