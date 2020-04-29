# -*- coding: utf8 -*-

import logging
logger = logging.getLogger('debug')


class Breadcrumbs:
    """

    """

    def __init__(self):
        """
        from myfirm.utils import breadcrumbs
        bc = breadcrumbs.Breadcrumbs()
        breadcrumbs = bc.home()

        breadcrumbs.append({'name': 'Home', 'url': 'invoices_main'})
        """
        self.breadcrumbs = []

    def add_one(self, name, url):
        """

        :param name:
        :param url:
        :return:
        """
        self.breadcrumbs.append({'name': name, 'url': url})

    def home(self):
        """
        breadcrumbs.append({'name': 'Home', 'url': 'invoices_main'})
        :return:
        """
        self.breadcrumbs = []
        self.add_one('Task', 'index')
        self.add_one('Home', 'invoices_main')
        return self.breadcrumbs

    def myfirm(self):
        """
        breadcrumbs.append({'name': 'moja firma', 'url': None})
        :return:
        """
        self.home()
        self.add_one('moja firma', 'myfirm_main')
        return self.breadcrumbs

    def customers(self):
        """
        # breadcrumbs.append({'name': 'klienci', 'url': 'customers_main'})

        :return:
        """
        self.home()
        self.add_one('klienci', 'customers_main')
        return self.breadcrumbs

    def customer_one(self, klient='klient'):
        """
        # breadcrumbs.append({'name': 'klient', 'url': None})
        :return:
        """
        self.customers()
        self.add_one(klient, None)
        return self.breadcrumbs

    def invoices(self):
        """
        # breadcrumbs.append({'name': 'lista faktur', 'url': 'invoices_list'})
        :return:
        """
        self.home()
        self.add_one('faktury', 'invoices_list')
        return self.breadcrumbs

    def invoice_one(self, invoice='faktura'):
        """
        # breadcrumbs.append({'name': 'faktura', 'url': None})
        :return:
        """
        self.invoices()
        self.add_one(invoice, None)
        return self.breadcrumbs

    def items(self):
        """
        # breadcrumbs.append({'name': 'Items', 'url': None})
        :return:
        """
        self.home()
        self.add_one('towary', 'items_list')
        return self.breadcrumbs

