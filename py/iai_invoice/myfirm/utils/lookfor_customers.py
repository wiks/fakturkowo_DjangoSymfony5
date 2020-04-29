# -*- coding: utf8 -*-

import logging
from myfirm.models import FirmData

logger = logging.getLogger('debug')


class LookforCustomers:
    """

    """

    def lookfor_customers(self, lookfor):
        """

        :param lookfor:
        :return:
        """
        """

            :param lookfor:
            :return:
            """
        result = []
        if len(lookfor) >= 3:

            firm_objs_list = []

            firm_data_name_objs = FirmData.objects.filter(fname__contains=lookfor).values_list('id', flat=True)
            # logger.debug('firm_data_name_objs: %s', firm_data_name_objs)
            if firm_data_name_objs:
                for one in firm_data_name_objs:
                    if one not in firm_objs_list:
                        firm_objs_list.append(one)

            firm_data_nip_objs = FirmData.objects.filter(nip__contains=lookfor).values_list('id', flat=True)
            # logger.debug('firm_data_nip_objs: %s', list(firm_data_nip_objs))
            for one in firm_data_nip_objs:
                if one not in firm_objs_list:
                    firm_objs_list.append(one)

            firm_data_pesel_objs = FirmData.objects.filter(pesel__contains=lookfor).values_list('id', flat=True)
            # logger.debug('firm_data_pesel_objs: %s', firm_data_pesel_objs)
            for one in firm_data_pesel_objs:
                if one not in firm_objs_list:
                    firm_objs_list.append(one)

            firm_data_regon_objs = FirmData.objects.filter(regon__contains=lookfor).values_list('id', flat=True)
            # logger.debug('firm_data_regon_objs: %s', firm_data_regon_objs)
            for one in firm_data_regon_objs:
                if one not in firm_objs_list:
                    firm_objs_list.append(one)

            if firm_objs_list:
                firm_objs_list = firm_objs_list[:5]
                for id in firm_objs_list:
                    firm_obj = FirmData.objects.filter(id=id) \
                        .values_list('id', 'fname', 'nip', 'pesel', 'regon').first()
                    if firm_obj:
                        result.append(firm_obj)
        return result

