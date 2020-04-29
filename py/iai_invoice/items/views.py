# -*- coding: utf8 -*-

import logging
# from django.utils import timezone
# from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from items.models import Items
# from invoices.models import Vats
# from myfirm.models import FirmData
# from myfirm.utils import myfirm_parser
# from invoices.utils import invoice_parser
# from invoices.utils import invoices_common
# from iai_invoice.utils import validation_invoice
from myfirm.utils import breadcrumbsutil
logger = logging.getLogger('debug')


def items_list(request):
    """

    :param request:
    :return:
    """
    response = None
    web_context = {}
    bc = breadcrumbsutil.Breadcrumbs()
    breadcrumbs = bc.items()
    web_context['breadcrumbs'] = breadcrumbs

    if request.method == 'POST':
        action = request.POST.get('action')
        logger.debug('action... --> %s', action)
        if action == 'Cancel':
            response = redirect('invoices_main')

    items_objs = Items.objects.all().order_by('name')
    # --------- paginator -----------------------------
    page = request.GET.get('page', 1)
    max_items_per_page = 10
    paginator = Paginator(items_objs, max_items_per_page)
    try:
        range_answers_with_opinion = paginator.page(page)
    except PageNotAnInteger:
        range_answers_with_opinion = paginator.page(1)
    except EmptyPage:
        range_answers_with_opinion = paginator.page(paginator.num_pages)
    web_context['corected_pagination'] = range_answers_with_opinion
    web_context['paginator'] = paginator
    # --------- paginator -----------------------------
    # web_context['items_list'] = items_objs
    web_context['items_list'] = range_answers_with_opinion

    if not response:
        response = render(request, 'items/items_list.html', web_context)
    return response

