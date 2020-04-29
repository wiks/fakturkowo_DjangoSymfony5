# -*- coding: utf8 -*-

import json
from django.http import JsonResponse
import logging
from myfirm.utils import lookfor_items
from myfirm.utils import lookfor_customers


logger = logging.getLogger('debug')


def angular_url(request):
    """
    wyszukiwanie nabywców
    :param request:
    :return:
    """
    result = []
    lookfor = None
    category = None
    if request.method == 'POST':
        r = json.loads(request.body.decode('utf-8'))
        # logger.debug('r: %s', r)
        if r and 'category' in r and 'lookfor' in r:
            category = r['category']
            lookfor = r['lookfor']
            logger.debug('category: %s, lookfor: %s', category, lookfor)

        # --------------------------- część odpowiedzialna za wyszukiwanie firmy ----------------------------------
        if lookfor and category == 'customer' and len(lookfor) >= 3:
            lfc = lookfor_customers.LookforCustomers()
            result = lfc.lookfor_customers(lookfor)
        # --------------------------- część odpowiedzialna za wyszukiwanie firmy ----------------------------------

        # --------------------------- część odpowiedzialna za wyszukiwanie towaru ---------------------------------
        if lookfor and category == 'item':
            lfi = lookfor_items.LookforItems()
            result = lfi.lookfor_items(lookfor)
        # --------------------------- część odpowiedzialna za wyszukiwanie towaru ---------------------------------

    logger.debug('res: %s', result)
    return JsonResponse(result, safe=False)
