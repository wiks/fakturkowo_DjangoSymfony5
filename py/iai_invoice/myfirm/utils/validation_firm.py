# -*- coding: utf8 -*-

import json
import re
import logging

logger = logging.getLogger('debug')


class ValidationFirm:
    """

    """

    def __init__(self):
        """
        """
        pass
    
    def validate_complet_firm_data(self, *args):
        """
        """
        # logger.debug('%s %s %s %s %s %s %s %s %s %s %s ',
        #              firmName, firmAdres1, firmAdres2, firmAdres3, firmAdres4, firmAdres5,
        #              mInputEmail, firmNip, firmRegon, firmPesel, firmAccount1, firmAccount2)
        errors_message_list = []
        errors_message_redclass_list = []

        fname, \
            errors_message = self.fname(args[0])
        if errors_message:
            errors_message_list.append(errors_message)
            errors_message_redclass_list.append('firmName')

        address_json, \
            errors_message = self.address(args[1], args[2], args[3], args[4], args[5])
        if errors_message:
            errors_message_list.append(errors_message)
            errors_message_redclass_list.append('firmAdres')

        email = None
        if args[6]:
            email, \
                errors_message = self.vemail(args[6])
            if errors_message:
                errors_message_list.append(errors_message)
                errors_message_redclass_list.append('mInputEmail')
        nip = None
        if args[7]:
            nip, \
                errors_message = self.nip(args[7])
            if errors_message:
                errors_message_list.append(errors_message)
                errors_message_redclass_list.append('firmNip')

        regon = None
        if args[8]:
            regon, \
                errors_message = self.regon(args[8])
            if errors_message:
                errors_message_list.append(errors_message)
                errors_message_redclass_list.append('firmRegon')

        pesel = None
        if args[9]:
            pesel, \
                errors_message = self.pesel(args[9])
            if errors_message:
                errors_message_list.append(errors_message)
                errors_message_redclass_list.append('firmPesel')

        if not nip and not regon and not pesel:
            errors_message = 'Wymagany jest jeden z: NIP, REGON, PESEL'
            errors_message_list.append(errors_message)

        bank_json, \
            errors_message = self.bank(args[10], args[11])
        if errors_message:
            errors_message_list.append(errors_message)
            errors_message_redclass_list.append('firmAccount')

        return fname, \
               address_json, \
               email,\
               nip, \
               regon, \
               pesel, \
               bank_json, \
               errors_message_list, \
               errors_message_redclass_list

    def fname(self, fname):
        """

        :param fname:
        :return:
        """
        ret = fname
        errors_message = None
        if not fname:
            errors_message = 'Przydałaby się nazwa firmy'
        return ret, errors_message

    def address(self, *args):
        """

        :return:
        """
        errors_message = 'Proszę wprowadzić choć jedną linię adresu'

        address_list = []
        logger.debug('args: %s', args)
        # DEBUG 2020-04-23 13:12:42,115 myvalidation args: ('qweqwe', 'qweqweqwe', 'qweqweqweqwe', '', '')
        for arg in args:
            if arg:
                errors_message = None
                address_list.append(arg)

        address_json = json.dumps(address_list)
        return address_json, \
               errors_message

    def vemail(self, email):
        """

        :param email:
        :return:
        """
        ret = email
        errors_message = 'wprowadzony EMAIL nie jest poprawny'
        if re.match(r"^[\w\.\+\-]+\@[\w\-]+\.[a-z]{2,3}$", email):
            errors_message = None
        return ret, \
               errors_message

    def nip(self, nip):
        """
        https://blog.aleksander.kaweczynski.pl/walidacja-numerow-pesel-nip-regon-w-javascript-i-php/

        :param nip:
        :return:
        """
        ret = nip
        errors_message = 'wprowadzony NIP nie jest poprawny'
        digits = nip.strip().replace('-', '')
        if re.match('\d{10}', digits):
            logger.debug('NIP sprawdzam... %s', list(digits) )
            checksum = 0
            ct = [6, 5, 7, 2, 3, 4, 5, 6, 7]
            for i in range(len(ct)):
                checksum += (int(digits[i]) * ct[i])
            checksum = checksum % 11
            # logger.debug('checksum: %s', checksum)
            if int(digits[len(ct)]) == checksum:
                ret = digits
                logger.debug('NIP poprawny')
                errors_message = None
        return ret, errors_message

    def regon(self, regon):
        """
        poprawne REGONY:
        123456785
        12345678512347
        https://pl.wikipedia.org/wiki/REGON
        :param regon:
        :return:
        """
        ret = regon
        ct = None
        errors_message = 'wprowadzony REGON nie jest poprawny'
        if re.match('\d{9}$', regon):
            regon = regon.strip()
            logger.debug('REGON9 sprawdzam... %s', list(regon))
            ct = [8, 9, 2, 3, 4, 5, 6, 7]
        if re.match('\d{14}$', regon):
            regon = regon.strip()
            logger.debug('REGON14 sprawdzam... %s', list(regon))
            ct = [2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8]
        if ct:
            checksum = 0
            for i in range(len(ct)):
                checksum += (int(regon[i]) * ct[i])
            checksum = checksum % 11
            # logger.debug('checksum: %s', checksum)
            if int(regon[len(ct)]) == checksum:
                logger.debug('REGON poprawny')
                errors_message = None
        return ret, errors_message

    def pesel(self, pesel):
        """
        71050103357
        :param pesel:
        :return:
        """
        ret = pesel
        errors_message = 'wprowadzony PESEL nie jest poprawny'
        if re.match('\d{11}$', pesel):
            logger.debug('PESEL sprawdzam...')
            pesel = pesel.strip()
            checksum = 0
            ct = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
            for i in range(len(ct)):
                checksum += (int(pesel[i]) * ct[i])
            if not checksum % 10:
                ret = pesel
                logger.debug('PESEL poprawny')
                errors_message = None
        return ret, \
               errors_message

    def bank(self, *args):
        """

        75 1020 4870 0000 5602 0076 5859

        https://pl.wikipedia.org/wiki/Numer_rachunku_bankowego
        CC AAAA AAAA BBBB BBBB BBBB BBBB
        http://phpedia.pl/wiki/Walidacja_numeru_NRB
        :param *args:
        :return:
        """
        bank_list = []
        errors_message = 'wprowadzony numer konta bankowego nie jest poprawny'
        for arg in args:
            if arg:
                bank_list.append(arg.strip())
        if bank_list:
            # logger.debug('bank account number validation: %s', bank_list[0])
            if re.match('\d{2} \d{4} \d{4} \d{4} \d{4} \d{4} \d{4}$', bank_list[0]) \
                    or re.match('\d{26}$', bank_list[0]):
                logger.debug('NR KONTA sprawdzam...')
                account_number26 = bank_list[0].replace(' ', '')
                # logger.debug('bank account number validation: %s', account_number26)
                ct = [1, 10,
                      3, 30, 9, 90,
                      27, 76, 81, 34,
                      49, 5, 50, 15,
                      53, 45, 62, 38,
                      89, 17, 73, 51,
                      25, 56, 75, 71,
                      31, 19, 93, 57]
                # $iNRB = substr($iNRB, 2).substr($iNRB, 0, 2);
                # od drugiego znaku . na końcu dwa ostatnie znaki
                account_number26_reorgan = account_number26[2:] + '2521' + account_number26[:2]
                # logger.debug('bank account number validation: %s', account_number26_reorgan)
                # DEBUG 2020-04-23 15:25:23,303 myvalidation bank account number validation:
                # 75102048700000560200765859
                # DEBUG 2020-04-23 15:25:23,303 myvalidation bank account number validation:
                # 102048700000560200765859252175
                checksum = 0
                for i in range(len(ct)):
                    checksum += int(account_number26_reorgan[len(ct) - 1 - i]) * ct[i]
                if checksum % 97 == 1:
                    logger.debug('BANK poprawny')
                    errors_message = None
        bank_json = json.dumps(bank_list)
        return bank_json, \
               errors_message

