# -*- coding: utf8 -*-

"""
do utworzenia towarów, wylosowania VAT i jednostek i cen
"""

from items.models import Items
from items.models import Jms
from items.models import Vats
import random


class MakeIt:
    """

    """
    def __init__(self):
        """

        """
        self.vat_obj_list = Vats.objects.all()
        self.jm_obj_list = Jms.objects.all()

    def random_one_od_list(self, sequence):
        """

        :param inlist:
        :return:
        """
        # listlen = len(sequence)
        # index = random(listlen)
        return random.choice(sequence)

    def doit(self):
        """
        utwórz przedmioty z listy
        :return:
        """
        list = [
            'jabłka',
            'pomarańcze',
            'banany',
            'truskawki',
            'awokado',
            'pomidory',
            'ananas',
            'grejpfrut',
            'cytryny',
            'mleko o niskiej zawartości tłuszczu',
            'jogurt',
            'jajka',
            'twarożek',
            'ser żółty',
            'masło',
            'miód',
            'pierś z kurczaka',
            'szynka z indyka',
            'owoce morza',
            'łosoś',
            'dorsz',
            'sól',
            'cukier',
            'cynamon',
            'kolendra',
            'oregano',
            'czarny pieprz',
            'czosnek',
            'goździki',
            'kminek',
            'imbir',
            'pietruszka',
            'kolendra',
            'liście bazylii',
            'ketchup',
            'musztarda',
            'cebula',
            'ziemniaki',
            'brokuły',
            'marchew',
            'buraki',
            'szpinak',
            'papryka',
            'sałata',
            'seler',
            'ogórek',
            'ciecierzyca',
            'fasola',
            'soja',
            'olej sezamowy',
            'olej rzepakowy',
            'oliwa z oliwek',
            'migdały',
            'nasiona lnu',
            'orzeszki ziemne',
            'orzechy włoskie',
            'słonecznik',
            'masło orzechowe',
            'dżem',
            'koncentrat pomidorowy',
            'pomidory w puszce',
            'tofu',
            'pasztet roślinny',
            'daktyle',
            'rodzynki suszone',
            'hummus',
            'mąka',
        ]
        for one in list:
            item_obj = Items.objects.filter(name=one).first()
            if not item_obj:
                item_obj = Items()
                item_obj.name = one
                item_obj.price_netto = float(random.randint(1, 10000)) / 10
                item_obj.vat = self.random_one_od_list(self.vat_obj_list)
                item_obj.jm = self.random_one_od_list(self.jm_obj_list)
                item_obj.save()


if __name__ == "__main__":

    mi = MakeIt()
    mi.doit()

'''
python manage.py shell
from items.utils import makeit 
mi = makeit.MakeIt()
mi.doit()
exit()

'''
