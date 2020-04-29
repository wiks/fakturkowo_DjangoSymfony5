# -*- coding: utf8 -*-

import logging
from items.models import Items

logger = logging.getLogger('debug')


class LookforItems:
    """

    """

    def lookfor_items(self, lookfor):
        """

        :param lookfor:
        :return:
        """
        result = []
        if len(lookfor) >= 3:
            items_objs = Items.objects.filter(name__contains=lookfor).values_list('id', 'name')[:5]
            result = []
            for item_obj in items_objs:
                result.append(list(item_obj))
        return result
