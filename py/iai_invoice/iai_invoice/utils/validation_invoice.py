# -*- coding: utf8 -*-

# import json
# import re
# from items.models import Vats
from invoices.models import Invoices
import logging

logger = logging.getLogger('debug')


class ValidationInvoice:
    """

    """

    def __init__(self):
        """

        """
        pass

    def validate_complet_invoice_data(self, invoice_obj, *args):
        """

        0 fNr,
        1 person_auth_name,
        2 dt_created,
        3 dt_pait_to,
        4 dt_delivery

        :param args:
        :return:
        """
        errors_message_list = []
        errors_message_redclass_list = []

        # numer faktury potrzebny dla sprawdzenia, czy nie dublujemy numeru innej faktury (prócz tej właśnie)
        fid = None
        if invoice_obj and invoice_obj.id:
            fid = invoice_obj.id
        fv_fNr, \
            errors_message = self.fvat_nr(args[0], fid)
        if errors_message:
            errors_message_list.append(errors_message)
            errors_message_redclass_list.append('fNr')

        fv_person_auth_name = args[1]
        dt_created = args[2]
        dt_pait_to = args[3]
        dt_deliver = args[4]

        return fv_fNr, \
               fv_person_auth_name, \
               dt_created, \
               dt_pait_to, \
               dt_deliver, \
               errors_message_list, \
               errors_message_redclass_list

    # def validate_complet_invoice_data0(self, *args):
    #     """
    #
    #     name,
    #     items_number,
    #     fNr,
    #     bruttonetto,
    #     vat,
    #     price_sum_netto,
    #     price_sum_brutto,
    #     person_auth_name
    #
    #     :param args:
    #     :return:
    #     """
    #     errors_message_list = []
    #     errors_message_redclass_list = []
    #
    #     fv_name, \
    #         errors_message = self.fname(args[0])
    #     if errors_message:
    #         errors_message_list.append(errors_message)
    #         errors_message_redclass_list.append('name')
    #
    #     fv_items_number = int(args[1])
    #     fv_fNr = args[2]
    #
    #     vat_obj, \
    #         fv_price_sum_brutto, \
    #         fv_price_sum_netto, \
    #         errors_message = self.price(args[3], args[4], args[5], args[6])
    #     if errors_message:
    #         errors_message_list.append(errors_message)
    #         errors_message_redclass_list.append('price')
    #
    #     fv_person_auth_name = args[7]
    #
    #     dt_created = args[8]
    #     dt_pait_to = args[9]
    #     dt_deliver = args[10]
    #
    #     return fv_name, \
    #            fv_items_number, \
    #            fv_fNr, \
    #            vat_obj, \
    #            fv_price_sum_netto, \
    #            fv_price_sum_brutto, \
    #            fv_person_auth_name, \
    #            dt_created, \
    #            dt_pait_to, \
    #            dt_deliver, \
    #            errors_message_list, \
    #            errors_message_redclass_list

    def fvat_nr(self, fNr, fid):
        """
        sprawdż w bazie danych, czy nie ma już takiego numeru faktury,
        z wyłaczeniem obecnego IDfaktury
        :param fNr:
        :param fid:
        :return:
        """
        ret = fNr
        errors_message = 'proszę nadać numer fakturze'
        if fNr:
            invoice_obj = Invoices.objects.filter(nr=fNr).exclude(id=fid).first()
            if invoice_obj:
                errors_message = 'istnieje już faktura o takim numerze, podaj inny'
            else:
                errors_message = None
                ret = fNr
        return ret, errors_message

    # def fname(self, fname):
    #     """
    #
    #     :param fname:
    #     :return:
    #     """
    #     ret = fname
    #     errors_message = None
    #
    #     return ret, errors_message

    # def price(self, bruttonetto, fv_vat, price_sum_netto, price_sum_brutto):
    #     """
    #
    #     'bruttonetto': ['brutto'],
    #     'vat': ['7'],
    #     'price_sum_netto': [''],
    #     'price_sum_brutto': ['99'],
    #
    #     :param fname:
    #     :return:
    #     """
    #     # logger.debug('bruttonetto %s, fv_vat %s, price_sum_netto %s, price_sum_brutto %s',
    #     # bruttonetto, fv_vat, price_sum_netto, price_sum_brutto)
    #     fv_price_sum_brutto = None
    #     fv_price_sum_netto = None
    #     errors_message = 'błąd przy określeniu kwoty wartości lub VAT'
    #     vat_obj = Vats.objects.filter(percent=fv_vat).first()
    #     if vat_obj:
    #         try:
    #             if bruttonetto == 'brutto':
    #                 fv_price_sum_brutto = round(float(price_sum_brutto), 2)
    #                 fv_price_sum_netto = round(fv_price_sum_brutto * 100 / (100 + vat_obj.percent), 2)
    #                 errors_message = None
    #             elif bruttonetto == 'netto':
    #                 fv_price_sum_netto = round(float(price_sum_netto), 2)
    #                 fv_price_sum_brutto = round(fv_price_sum_netto * (100 + vat_obj.percent) / 100, 2)
    #                 errors_message = None
    #         except Exception as e:
    #             # logger.debug('error PRICE validation: %s', e)
    #             pass
    #     # logger.debug('vat_obj %s, fv_price_sum_brutto %s, fv_price_sum_netto %s, errors_message %s',
    #     # vat_obj, fv_price_sum_brutto, fv_price_sum_netto, errors_message)
    #     return vat_obj, \
    #            fv_price_sum_brutto, \
    #            fv_price_sum_netto, \
    #            errors_message
