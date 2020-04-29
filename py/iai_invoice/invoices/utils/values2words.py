# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger('debug')

class DigitValues2words:
    """
    https://pl.python.org/forum/index.php?topic=4117.30
    35 nie działa
    """

    def __init__(self):
        """

        """
        self.units_list = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć",
                           "siedem", "osiem", "dziewięć"]
        self.dozens_list = ["", "dziesiec", "dzwadziescia", "trzydziesci", "czterdziesci",
                            "pięćdziesiąt", "szcześćdziesiąt", "siedemdziesiąt", "osiemdziesiąt",
                            "dziewięćdziesiat"]
        self.hundreads_of = ["", "sto", "dwieście", "trzysta", "czerysta", "pięćset",
                             "sześcset", "siedemset", "osiemset", "dziewięćset"]
        self.teens = ["dziesięc", "jedenascie", "dwanaście", "trzynaście",
                      "czternaście", "piętnaście", "szesznaście", "siediemanście",
                      "osiemnaście", "dziewiętnaście"]
        self.bigones = ["", "tysiąc", "milion", "miliard", "bilion", "biliard",
                        "trylion", "tryliard", "kwadrylion", "kwadryliard", "kwintylion"]

    def convert_it(self, list2convert):
        """

        :return:
        """

        result = ""
        while list2convert[0] == '0':
            list2convert = list2convert[1:]
            if len(list2convert) == 0:
                return (result)
        if len(list2convert) == 3:
            result += self.hundreads_of[int(list2convert[-3])] + " "
            list2convert = list2convert[1:]
            while list2convert and list2convert[0] == '0':
                list2convert = list2convert[1:]
        if len(list2convert) == 2:
            if list2convert[-2] == "1":
                result += self.teens[int(list2convert[-1])] + " "
                return result
            else:
                result += self.dozens_list[int(list2convert[-2])] + " "
                if int(list2convert[-1]):
                    result += self.units_list[int(list2convert[-1])] + " "
                return result
        if len(list2convert) == 1:
            result += self.units_list[int(list2convert[0])]
            return result
        return result

    def postscript(self, mylist, digits_length):
        """

        :param mylist:
        :param digits_length:
        :return:
        """
        if digits_length == 0:
            return ""
        a = 0
        b = 0
        c = 0
        if len(mylist) == 1:
            c = int(mylist[0])
        if len(mylist) == 2:
            b = int(mylist[0])
            c = int(mylist[1])
        if len(mylist) == 3:
            a = int(mylist[0])
            b = int(mylist[1])
            c = int(mylist[2])
        if a == 0 and b == 0 and c == 1:
            if digits_length == 1:
                return "tysiąc "
            else:
                return self.bigones[digits_length] + " "
        if b == 1:
            if digits_length == 1:
                return "tysięcy "
            else:
                return self.bigones[digits_length] + "ów "
        else:
            if c == 2 or c == 3 or c == 4:
                if digits_length == 1:
                    return "tysiące "
                else:
                    return self.bigones[digits_length] + "y "
            else:
                if digits_length == 1:
                    return "tysięcy "
                else:
                    return self.bigones[digits_length] + "ów "

    def translate(self, digits_value):
        """

        :param digits_as_string:
        :return:
        """
        result = ""
        if digits_value == 0:
            result = "zero"
            return result

        digits_as_string = str(digits_value)
        rest_of = len(digits_as_string) % 3
        digits_length = int((len(digits_as_string) - 1) / 3)
        if rest_of == 1:
            result += self.convert_it(digits_as_string[0]) + ' '
            result += self.postscript('0' + '0' + digits_as_string[0], digits_length)
            digits_length -= 1
            digits_as_string = digits_as_string[1:]
        if rest_of == 2:
            result += self.convert_it(digits_as_string[0] + digits_as_string[1])
            # logger.debug('digits_as_string[0] %s , digits_as_string[1] %s ', digits_as_string[0], digits_as_string[1])
            result += self.postscript('0' + digits_as_string[0] + digits_as_string[1], digits_length)
            digits_length -= 1
            digits_as_string = digits_as_string[2:]
        for i in range(0, len(digits_as_string), 3):
            result += self.convert_it(digits_as_string[i] + digits_as_string[i + 1] + digits_as_string[i + 2])
            if digits_as_string[i] != '0' or digits_as_string[i + 1] != '0' or digits_as_string[i + 2] != '0':
                result += self.postscript(digits_as_string[i] + digits_as_string[i + 1] + digits_as_string[i + 2], digits_length)
            digits_length -= 1
        return result

    def currency_translate(self, price):
        """

        :param price:
        :return:
        """
        integ = int(price)
        price_rest = int((price - integ) * 100)
        return self.translate(integ) + " " + str(price_rest) + "/100"


if __name__ == "__main__":

    d2w = DigitValues2words()

    # print(d2w.translate(35))
    for i in range(1000):
        print(str(i) + ' --> ' + d2w.translate(i))
