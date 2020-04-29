# -*- coding: utf8 -*-

import json
from myfirm.models import FirmData
from invoices.models import InvoicesItems
from items.models import Vats
import logging

logger = logging.getLogger('debug')


class InvoiceParser:
    """

    """

    def data_invoice_from_postrequest(self, request):
        """

        :param request:
        :return:
        """
        # DEBUG 2020-04-24 22:28:35,023 views <QueryDict: {'csrfmiddlewaretoken': ['46zwEUSugqMKEPH8pLh53ZxOIJSho4pMVO1Y563E6kkyQbPkUMMBOvApe1GOnj3d'],
        # 'name': ['usluga'],
        # 'items_number': ['2'],
        # 'fNr': ['23456'],
        # 'bruttonetto': ['brutto'],
        # 'vat': ['7'],
        # 'price_sum_netto': [''],
        # 'price_sum_brutto': ['99'],
        # 'dt_created': ['2020-04-24'],
        # 'dt_delivery': ['2020-05-23'],
        # 'dt_pait_to': ['2020-05-24'],
        # 'person_auth_name': ['joco'],
        # 'action': ['OK']}>
        # name = request.POST.get('name', None)
        # items_number = request.POST.get('items_number', 1)
        # if not items_number:
        #     items_number = 1
        fNr = request.POST.get('fNr', None)
        # bruttonetto = request.POST.get('bruttonetto', 0)
        # vat = request.POST.get('vat', None)
        # price_sum_netto = request.POST.get('price_sum_netto', None)
        paid_sum_brutto = request.POST.get('paid_sum_brutto', 0)
        if not paid_sum_brutto:
            paid_sum_brutto = 0
        person_auth_name = request.POST.get('person_auth_name', None)
        dt_created = request.POST.get('dt_created', None)
        dt_pait_to = request.POST.get('dt_pait_to', None)
        dt_delivery = request.POST.get('dt_delivery', None)

        pay_form_id = None  # todo przelew

        return fNr, \
               person_auth_name, \
               dt_created, \
               dt_pait_to, \
               dt_delivery, \
               paid_sum_brutto, \
               pay_form_id

    def from_request_to_webcontext_invoice(self,
                                           web_context,
                                           fNr,
                                           customer,
                                           seller,
                                           person_auth_name,
                                           dt_created,
                                           dt_pait_to,
                                           dt_delivery,
                                           paid_sum_brutto
                                           ):
        """

        :param web_context:
        :param fNr:
        :param customer:
        :param seller:
        :param invoices_items_objs:
        :param vat_sum:
        :param price_sum_netto:
        :param price_sum_brutto:
        :param person_auth_name:
        :param dt_created:
        :param dt_pait_to:
        :param dt_delivery:
        :param paid_sum_brutto:
        :return:
        """
        web_context['fNr'] = fNr
        web_context['customer'] = customer
        web_context['seller'] = seller
        # web_context['invoices_items_objs'] = invoices_items_objs
        # web_context['vat_sum'] = vat_sum
        web_context['paid_sum_brutto'] = paid_sum_brutto
        # web_context['price_sum_brutto'] = price_sum_brutto
        # web_context['paid_form'] = paid_form
        web_context['person_auth_name'] = person_auth_name
        web_context['dt_created'] = dt_created
        web_context['dt_pait_to'] = dt_pait_to
        web_context['dt_delivery'] = dt_delivery
        return web_context

    def from_request_to_webcontext_invoice0(self,
                                           web_context,
                                           name,
                                           items_number,
                                           fNr,
                                           vat,
                                           price_sum_netto,
                                           price_sum_brutto,
                                           person_auth_name,
                                           dt_created,
                                           dt_pait_to,
                                           dt_delivery
                                           ):
        """

        :return:
        """
        web_context['name'] = name
        web_context['items_number'] = items_number
        web_context['fNr'] = fNr
        # web_context['bruttonetto'] = bruttonetto
        web_context['vat'] = vat
        web_context['price_sum_netto'] = price_sum_netto
        web_context['price_sum_brutto'] = price_sum_brutto
        web_context['person_auth_name'] = person_auth_name
        web_context['dt_created'] = dt_created
        web_context['dt_pait_to'] = dt_pait_to
        web_context['dt_delivery'] = dt_delivery
        return web_context

    def invoice_pickup(self, invoice_obj):
        """
        pobierz obiekt,
        oraz dodane do faktury towary wraz z ilościami,
        przelicz kwoty i VATy
        :param invoice_obj:
        :return:
        """
        fNr = invoice_obj.nr
        dt_created = ''
        dt_pait_to = ''
        dt_delivery = ''
        if invoice_obj.dt_created:
            dt_created = invoice_obj.dt_created.strftime("%Y-%m-%d")
        if invoice_obj.dt_pait_to:
            dt_pait_to = invoice_obj.dt_pait_to.strftime("%Y-%m-%d")
        if invoice_obj.dt_delivery:
            dt_delivery = invoice_obj.dt_delivery.strftime("%Y-%m-%d")
        customer = FirmData.objects.filter(id=invoice_obj.customer_id).first()
        seller = FirmData.objects.filter(id=1).first()

        paid_form = 'przelew'
        # todo - dopracuj inne formy przelewy wg ID:
        # invoice_obj.pay_form_id = None  # None to przelew
        if invoice_obj.pay_form_id:
            paid_form = 'gotówka'

        person_auth_name  = invoice_obj.person_auth_name
        if not fNr:
            fNr = ''
        if not person_auth_name:
            person_auth_name = ''
        paid_sum_brutto = invoice_obj.paid_sum_brutto
        if not paid_sum_brutto:
            paid_sum_brutto = 0

        invoices_items_richer = []  # tutaj utworzę postać dla faktury
        price_sum_netto = 0  # podliczę sumę netto
        price_sum_brutto = 0  # podliczę sumę brutto
        # pobieram listę wszystkich dodanych do faktury produktów i ich liczbę
        invoices_items_objs = InvoicesItems.objects.filter(invoice=invoice_obj)

        # jeśli chodzi o VAT, łatwiej będzie podliczyć w tymczasowej tabeli:
        vat_tmp_dict = {}
        for vat_obj in Vats.objects.all().order_by('percent'):
            vat_tmp_dict[vat_obj.percent] = 0

        # muszę podliczyć VATy a także utworzyć wpisy dla faktury
        for invoices_item_obj in invoices_items_objs:
            # towar (cena i VAT, JM):
            vat = invoices_item_obj.items.vat.percent
            price_netto = round(float(invoices_item_obj.items.price_netto), 2)
            price_brutto = round(price_netto * float(100 + vat) / 100, 2)
            value_netto = round(price_netto * invoices_item_obj.items_number, 2)
            price_sum_netto += value_netto
            value_brutto = round(value_netto * float(100 + vat) / 100, 2)
            price_sum_brutto += value_brutto
            invoices_items_richer.append({
                'id': invoices_item_obj.id,
                'iid': invoices_item_obj.items.id,
                'name': invoices_item_obj.items.name,
                'items_number': invoices_item_obj.items_number,
                'jm': invoices_item_obj.items.jm.name,
                'price_netto': price_netto,
                'price_brutto': price_brutto,
                'value_netto' : value_netto,
                'vat': vat,
                'value_brutto': value_brutto,
            })
            # podliczam sumaryczny VAT:
            if vat not in vat_tmp_dict:
                vat_tmp_dict[vat] = 0
            vat_tmp_dict[vat] += value_netto

        # teraz tworzę resztę tabeli podliczenia VAT:
        vat_sum_list = []
        vat_sum_sum = {'wn': 0,
                       'wv': 0,
                       'wb': 0
                       }
        for vat, sum_netto in vat_tmp_dict.items():
            sum_brutto = round(sum_netto * float(100 + vat) / 100, 2)
            sum_netto = round(sum_netto, 2)
            vat_sum_one_row = {'sv': vat,
                               'wn': sum_netto,
                               'wv': round(sum_brutto - sum_netto, 2),
                               'wb': sum_brutto,
                               }
            vat_sum_list.append(vat_sum_one_row)
            vat_sum_sum['wn'] += vat_sum_one_row['wn']
            vat_sum_sum['wv'] += vat_sum_one_row['wv']
            vat_sum_sum['wb'] += vat_sum_one_row['wb']
        # podliczona tabela VAT:
        vat_sum_sum['wn'] = round(vat_sum_sum['wn'], 2)
        vat_sum_sum['wv'] = round(vat_sum_sum['wv'], 2)
        vat_sum_sum['wb'] = round(vat_sum_sum['wb'], 2)
        vat_sum = {
            'list': vat_sum_list,
            'sum': vat_sum_sum
        }
        # invoice_obj.price_sum_netto = price_sum_netto
        # invoice_obj.save()

        price_sum_netto = round(price_sum_netto, 2)
        price_sum_brutto = round(price_sum_brutto, 2)

        return fNr,  \
               customer, \
               seller, \
               invoices_items_richer, \
               vat_sum, \
               price_sum_netto, \
               price_sum_brutto, \
               paid_form, \
               person_auth_name, \
               dt_created, \
               dt_pait_to, \
               dt_delivery, \
               paid_sum_brutto

    # def invoice_pickup0(self, invoice_obj):
    #     """
    #
    #     :return:
    #     """
    #
    #     name = invoice_obj.name
    #     items_number = invoice_obj.items_number  # items_number
    #     fNr = invoice_obj.nr
    #
    #     vat = invoice_obj.vat.percent
    #
    #     price_sum_netto = invoice_obj.price_sum_netto
    #     price_sum_brutto = invoice_obj.price_sum_brutto
    #     person_auth_name  = invoice_obj.person_auth_name
    #     # price_sum_brutto = invoice_obj.price_sum_brutto
    #
    #     dt_created = ''
    #     dt_pait_to = ''
    #     dt_delivery = ''
    #     if invoice_obj.dt_created:
    #         dt_created = invoice_obj.dt_created.strftime("%Y-%m-%d")
    #     if invoice_obj.dt_pait_to:
    #         dt_pait_to = invoice_obj.dt_pait_to.strftime("%Y-%m-%d")
    #     if invoice_obj.dt_delivery:
    #         dt_delivery = invoice_obj.dt_delivery.strftime("%Y-%m-%d")
    #
    #     if not name:
    #         name = ''
    #     if not items_number:
    #         items_number = ''
    #     if not fNr:
    #         fNr = ''
    #     if not price_sum_netto:
    #         price_sum_netto = 0
    #     if not price_sum_brutto:
    #         price_sum_brutto = 0
    #     if not person_auth_name:
    #         person_auth_name = ''
    #
    #     customer = FirmData.objects.filter(id=invoice_obj.customer_id).first()
    #     seller = FirmData.objects.filter(id=1).first()
    #
    #     paid_form = 'przelew'
    #     # todo - dopracuj inne formy przelewy wg ID:
    #     # invoice_obj.pay_form_id = None  # None to przelew
    #     if invoice_obj.pay_form_id:
    #         paid_form = 'gotówka'
    #
    #     jm = 'sztt.'
    #     invoces_rows = []
    #     invoce_row = {'lp': 1,
    #                   'name': name,
    #                   'items_number': items_number,
    #                   'jm': jm,
    #                   'price_sum_netto': price_sum_netto,
    #                   'vat': vat,
    #                   'price_sum_brutto': price_sum_brutto,
    #                   }
    #     invoces_rows.append(invoce_row)
    #
    #     vat_sum_sum = {'wn': 0,
    #                    'wv': 0,
    #                    'wb': 0
    #                    }
    #     vat_sum_list = []
    #     vat_sum_one_row = {'sv': vat,
    #                        'wn': price_sum_netto,
    #                        'wv': price_sum_brutto - price_sum_netto,
    #                        'wb': price_sum_brutto,
    #                        }
    #     vat_sum_list.append(vat_sum_one_row)
    #     vat_sum_sum['wn'] += vat_sum_one_row['wn']
    #     vat_sum_sum['wv'] += vat_sum_one_row['wv']
    #     vat_sum_sum['wb'] += vat_sum_one_row['wb']
    #
    #     vat_sum = {
    #         'list': vat_sum_list,
    #         'sum': vat_sum_sum
    #     }
    #
    #     return customer, \
    #            seller, \
    #            invoces_rows, \
    #            vat_sum, \
    #            name,\
    #            items_number, \
    #            fNr,  \
    #            vat, \
    #            price_sum_netto, \
    #            price_sum_brutto, \
    #            paid_form, \
    #            person_auth_name, \
    #            dt_created, \
    #            dt_pait_to, \
    #            dt_delivery

    def update_webkontext(self, web_context, invoice_obj):
        """

        :return:
        """
        fNr, \
            customer, \
            seller, \
            invoices_items_richer, \
            vat_sum, \
            price_sum_netto, \
            price_sum_brutto, \
            paid_form, \
            person_auth_name, \
            dt_created, \
            dt_pait_to, \
            dt_delivery, \
            paid_sum_brutto = self.invoice_pickup(invoice_obj)

        web_context = self.from_request_to_webcontext_invoice(web_context,
                                                              fNr,
                                                              customer,
                                                              seller,
                                                              person_auth_name,
                                                              dt_created,
                                                              dt_pait_to,
                                                              dt_delivery,
                                                              paid_sum_brutto,
                                                              )
        return web_context

    def add_item_to_invoice(self, invoice_obj, item_obj, item_amount, errors_message_list):
        """
        dodaj przedmiot/pozycję do faktury
        :param invoice_obj:
        :param item_obj:
        :param item_amount:
        :param errors_message_list:
        :return:
        """
        invoices_item_obj = None
        item_amount_value = None
        if item_amount is None or item_amount.strip() == '':
            errors_message = 'proszę podać ilość w ' + str(item_obj.jm.name)
            errors_message_list.append(errors_message)
        else:
            try:
                item_amount_value = float(item_amount)
            except Exception as e:
                errors_message = 'proszę spróbować jeszcze raz'
                errors_message_list.append(errors_message)
            if item_amount_value:
                if item_amount_value < 0:
                    errors_message = 'wymagana wartość dodatnia'
                    errors_message_list.append(errors_message)
                else:
                    # jeśli jest w sztukach to nie może być ułamkiem...
                    kind_of_measure = item_obj.jm.id  # szt to ID=1
                    if kind_of_measure == 1:
                        logger.debug('tutaj musi być wartością całkowitą, bo dotyczy sztuk')
                        if item_amount_value - int(item_amount_value) != 0:
                            errors_message = 'proszę spróbować jeszcze raz, wymagana ilość sztuk'
                            errors_message_list.append(errors_message)
        if not errors_message_list and item_amount_value:
            logger.debug('dodajemy przedmiot do faktury')
            invoices_item_obj = InvoicesItems.objects.filter(invoice=invoice_obj,
                                                             items=item_obj,
                                                             ).first()
            if not invoices_item_obj:
                invoices_item_obj = InvoicesItems()
                invoices_item_obj.invoice = invoice_obj
                invoices_item_obj.items = item_obj
            invoices_item_obj.items_number = item_amount_value
            invoices_item_obj.save()
            # response = redirect('invoice_edit', invoice_obj.id)
        return invoices_item_obj, errors_message_list

