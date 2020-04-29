# -*- coding: utf8 -*-

import json

class MyFirmParser:
    """

    """

    def data_firm_from_postrequest(self, request):
        """

        :param request:
        :return:
        """
        address_list = [None, None, None, None, None]
        firm_account_list = [None, None]
        firmName = request.POST.get('firmName', None)
        address_list[0] = request.POST.get('firmAdres1', None)
        address_list[1] = request.POST.get('firmAdres2', None)
        address_list[2] = request.POST.get('firmAdres3', None)
        address_list[3] = request.POST.get('firmAdres4', None)
        address_list[4] = request.POST.get('firmAdres5', None)
        mInputEmail = request.POST.get('mInputEmail', None)
        firmNip = request.POST.get('firmNip', None)
        firmRegon = request.POST.get('firmRegon', None)
        firmPesel = request.POST.get('firmPesel', None)
        firm_account_list[0] = request.POST.get('firmAccount1', None)
        firm_account_list[1] = request.POST.get('firmAccount2', None)
        # logger.debug('%s %s %s %s %s %s %s %s %s %s %s %s',
        #              firmName, firmAdres1, firmAdres2, firmAdres3, firmAdres4, firmAdres5, mInputEmail,
        #              firmNip, firmRegon, firmPesel, firmAccount1, firmAccount2)
        return firmName, \
               address_list, \
               mInputEmail, \
               firmNip, \
               firmRegon, \
               firmPesel, \
               firm_account_list

    def myfirm_pickup(self, firm_data_obj):
        """

        :return:
        """
        firmName = firm_data_obj.fname
        try:
            address_list = json.loads(firm_data_obj.address_json)
            address_list += ['', '', '', '', '']
        except Exception as e:
            address_list = ['', '', '', '', '']
        address_list = address_list[:5]
        mInputEmail = firm_data_obj.email
        firmNip = firm_data_obj.nip
        firmRegon = firm_data_obj.regon
        firmPesel = firm_data_obj.pesel
        try:
            firm_account_list = json.loads(firm_data_obj.bank_account)
            firm_account_list += ['', '']
        except Exception as e:
            firm_account_list = ['', '']
        firm_account_list = firm_account_list[:2]

        if not firmName:
            firmName = ''
        if not mInputEmail:
            mInputEmail = ''
        if not firmNip:
            firmNip = ''
        if not firmRegon:
            firmRegon = ''
        if not firmPesel:
            firmPesel = ''
        return firmName, address_list, mInputEmail, firmNip, firmRegon, firmPesel, firm_account_list

    def from_request_to_webcontext_firm(self,
                                        web_context,
                                        firmName,
                                        address_list,
                                        mInputEmail,
                                        firmNip,
                                        firmRegon,
                                        firmPesel,
                                        firm_account_list):
        """

        :return:
        """
        web_context['firmName'] = firmName
        web_context['firmAdres1'] = address_list[0]
        web_context['firmAdres2'] = address_list[1]
        web_context['firmAdres3'] = address_list[2]
        web_context['firmAdres4'] = address_list[3]
        web_context['firmAdres5'] = address_list[4]
        web_context['mInputEmail'] = mInputEmail
        web_context['firmNip'] = firmNip
        web_context['firmRegon'] = firmRegon
        web_context['firmPesel'] = firmPesel
        web_context['firmAccount1'] = firm_account_list[0]
        web_context['firmAccount2'] = firm_account_list[1]
        return web_context

    def update_webkontext(self, web_context, firm_data_obj):
        """

        :return:
        """
        firmName, \
            address_list, \
            mInputEmail, \
            firmNip, \
            firmRegon, \
            firmPesel, \
            firm_account_list = self.myfirm_pickup(firm_data_obj)

        web_context = self.from_request_to_webcontext_firm(web_context,
                                                           firmName,
                                                           address_list,
                                                           mInputEmail,
                                                           firmNip,
                                                           firmRegon,
                                                           firmPesel,
                                                           firm_account_list)
        return web_context

    # def data_invoice_from_postrequest(self, request):
    #     """
    #
    #     :param request:
    #     :return:
    #     """
    #     # DEBUG 2020-04-24 22:28:35,023 views <QueryDict: {'csrfmiddlewaretoken': ['46zwEUSugqMKEPH8pLh53ZxOIJSho4pMVO1Y563E6kkyQbPkUMMBOvApe1GOnj3d'],
    #     # 'name': ['usluga'],
    #     # 'items_number': ['2'],
    #     # 'fNr': ['23456'],
    #     # 'bruttonetto': ['brutto'],
    #     # 'vat': ['7'],
    #     # 'price_sum_netto': [''],
    #     # 'price_sum_brutto': ['99'],
    #     # 'dt_created': ['2020-04-24'],
    #     # 'dt_delivery': ['2020-05-23'],
    #     # 'dt_pait_to': ['2020-05-24'],
    #     # 'person_auth_name': ['joco'],
    #     # 'action': ['OK']}>
    #     name = request.POST.get('name', None)
    #     items_number = request.POST.get('items_number', 1)
    #     fNr = request.POST.get('fNr', None)
    #     bruttonetto = request.POST.get('bruttonetto', 0)
    #     vat = request.POST.get('vat', None)
    #     price_sum_netto = request.POST.get('price_sum_netto', None)
    #     price_sum_brutto = request.POST.get('price_sum_brutto', None)
    #     person_auth_name = request.POST.get('person_auth_name', None)
    #     dt_created = request.POST.get('dt_created', None)
    #     dt_pait_to = request.POST.get('dt_pait_to', None)
    #     dt_delivery = request.POST.get('dt_delivery', None)
    #     return name, \
    #            items_number, \
    #            fNr, \
    #            bruttonetto, \
    #            vat, \
    #            price_sum_netto, \
    #            price_sum_brutto, \
    #            person_auth_name, \
    #            dt_created, \
    #            dt_pait_to, \
    #            dt_delivery
    #
    # def from_request_to_webcontext_invoice(self,
    #                                        web_context,
    #                                        name,
    #                                        items_number,
    #                                        fNr,
    #                                        bruttonetto,
    #                                        vat,
    #                                        price_sum_netto,
    #                                        price_sum_brutto,
    #                                        person_auth_name,
    #                                        dt_created,
    #                                        dt_pait_to,
    #                                        dt_delivery
    #                                        ):
    #     """
    #
    #     :return:
    #     """
    #     web_context['name'] = name
    #     web_context['items_number'] = items_number
    #     web_context['fNr'] = fNr
    #     web_context['bruttonetto'] = bruttonetto
    #     web_context['vat'] = vat
    #     web_context['price_sum_netto'] = price_sum_netto
    #     web_context['price_sum_brutto'] = price_sum_brutto
    #     web_context['person_auth_name'] = person_auth_name
    #     web_context['dt_created'] = dt_created
    #     web_context['dt_pait_to'] = dt_pait_to
    #     web_context['dt_delivery'] = dt_delivery
    #     return web_context

