# -*- coding: utf8 -*-

from datetime import datetime, timedelta
from django.shortcuts import render
from django.shortcuts import redirect
import logging
from invoices.models import Invoices
from invoices.models import InvoicesItems
from myfirm.utils import myfirm_parser
from invoices.utils import invoice_parser
from invoices.utils import values2words

logger = logging.getLogger('debug')


class InvoicesCommon:
    """

    """

    def create_empty_invoice(self, customer_id):
        """

        :param customer_id:
        :return:
        """
        # kasuję nieistniejące, niedokończone (todo zapis wymaga podania jednak numeru)
        # Invoices.objects.filter(nr__isnull=True).delete()
        dt_now = datetime.now()
        dt_future = dt_now + timedelta(days=30)

        invoice_obj = Invoices()
        invoice_obj.nr = None
        invoice_obj.customer_id = customer_id
        invoice_obj.price_sum_brutto = 0
        invoice_obj.price_sum_netto = 0
        invoice_obj.paid_sum_brutto = 0
        invoice_obj.pay_form_id = None
        invoice_obj.dt_created = dt_now.strftime("%Y-%m-%d")
        invoice_obj.dt_pait_to = dt_future.strftime("%Y-%m-%d")
        invoice_obj.dt_delivery = dt_future.strftime("%Y-%m-%d")
        invoice_obj.save()
        return invoice_obj

    def common_invoice_middle_show(self, web_context, invoice_obj):
        """

        :param web_context:
        :param invoice_obj:
        :return:
        """
        ddp = myfirm_parser.MyFirmParser()
        inp = invoice_parser.InvoiceParser()
        web_context['fNr'],\
            customer, \
            seller, \
            web_context['invoices_items_richer'], \
            web_context['vat_sum'], \
            web_context['price_sum_netto'], \
            price_sum_brutto, \
            web_context['paid_form'], \
            web_context['person_auth_name'], \
            web_context['dt_created'], \
            web_context['dt_pait_to'], \
            web_context['dt_delivery'], \
            web_context['paid_sum_brutto'] = inp.invoice_pickup(invoice_obj)
        web_context['price_sum_brutto'] = price_sum_brutto  # do tłumaczenia na słowną wartość

        shortfirm_seller = {}
        shortfirm_seller['firmName'], \
            shortfirm_seller['address_list'], \
            shortfirm_seller['mInputEmail'], \
            shortfirm_seller['firmNip'], \
            shortfirm_seller['firmRegon'], \
            shortfirm_seller['firmPesel'], \
            shortfirm_seller['firm_account_list'] = ddp.myfirm_pickup(seller)
        web_context['shortfirm_seller'] = shortfirm_seller

        shortfirm_customer = {}
        shortfirm_customer['firmName'], \
            shortfirm_customer['address_list'], \
            shortfirm_customer['mInputEmail'], \
            shortfirm_customer['firmNip'], \
            shortfirm_customer['firmRegon'], \
            shortfirm_customer['firmPesel'], \
            shortfirm_customer['firm_account_list'] = ddp.myfirm_pickup(customer)
        web_context['shortfirm_customer'] = shortfirm_customer
        # przetłumacz na słownie:
        v2w = values2words.DigitValues2words()
        web_context['price_sum_brutto_translated'] = v2w.currency_translate(price_sum_brutto)
        return web_context

    # def edit_item_add_part(self, request, web_context, invoice_obj, item_obj):
    #     """
    #     część widoku, odpowiedzialna za operacja zw. z dodawaniem rzeczy
    #     :param request:
    #     :param web_context:
    #     :param invoice_obj:
    #     :param item_obj:
    #     :return:
    #     """
    #     response = None
    #     errors_message_list = []
    #     web_context['item'] = item_obj
    #
    #     if request.method == 'POST':
    #         action = request.POST.get('action')
    #         logger.debug('action... --> %s', action)
    #         if action == 'Cancel':
    #             response = redirect('invoices_main')
    #         if action == 'OK':
    #             logger.debug('%s', request.POST)
    #
    #             item_amount_value = None
    #             item_amount = request.POST.get('item_amount', None)
    #
    #             if item_amount is None or item_amount.strip() == '':
    #                 errors_message = 'proszę podać ilość w ' + str(item_obj.jm.name)
    #                 errors_message_list.append(errors_message)
    #             else:
    #                 try:
    #                     item_amount_value = float(item_amount)
    #                 except Exception as e:
    #                     errors_message = 'proszę spróbować jeszcze raz'
    #                     errors_message_list.append(errors_message)
    #                 if item_amount_value:
    #                     if item_amount_value < 0:
    #                         errors_message = 'wymagana wartość dodatnia'
    #                         errors_message_list.append(errors_message)
    #                     else:
    #                         # jeśli jest w sztukach to nie może być ułamkiem...
    #                         kind_of_measure = item_obj.jm.id  # szt to ID=1
    #                         if kind_of_measure == 1:
    #                             logger.debug('tutaj musi być wartością całkowitą, bo dotyczy sztuk')
    #                             if item_amount_value - int(item_amount_value) != 0:
    #                                 errors_message = 'proszę spróbować jeszcze raz, wymagana wartość całkowita'
    #                                 errors_message_list.append(errors_message)
    #             if not errors_message_list and item_amount_value:
    #                 logger.debug('dodajemy przedmiot do faktury')
    #                 invoices_items_obj = InvoicesItems.objects.filter(invoice=invoice_obj,
    #                                                                   items=item_obj,
    #                                                                   ).first()
    #                 if not invoices_items_obj:
    #                     invoices_items_obj = InvoicesItems()
    #                     invoices_items_obj.invoice = invoice_obj
    #                     invoices_items_obj.items = item_obj
    #                 invoices_items_obj.items_number = item_amount_value
    #                 invoices_items_obj.save()
    #                 logger.debug('dodany/updatowany przedmiot do faktury %s', invoices_items_obj)
    #                 response = redirect('invoice_edit', invoice_obj.id)
    #             web_context['errors_message_list'] = errors_message_list
    #     if not response:
    #         response = render(request, 'invoices/invoice_edit_add_item.html', web_context)
    #     return response

