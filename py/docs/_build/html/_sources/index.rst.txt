.. IAI-invoice documentation master file, created by
   sphinx-quickstart on Thu Apr 23 09:10:17 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to IAI-invoice's documentation!
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Zajawka dokumentacji do zadania IAI / IdoSell.

Treść zadania:

w związku z tym prosimy o przygotowanie i przesłanie do środy, 29.04.2020 do godziny 12:30 następującego materiału:
Celem zadania jest napisanie skryptu PHP do wystawiania faktur. Minimalna funkcjonalność:


- wystawienie dokumentu dla klienta (dane podane w inputach z klawiatury)

- przypisanie pozycji do faktury

- nadanie numeru, daty,

- lista wystawionych faktur

- usuwanie faktur

Do powyższej funkcjonalności można dopisać szereg usprawnień, wykorzystać dowolny framework. Każdy dodatkowy element jest atutem podczas oceny. Realizacja minimalnej funkcjonalności jest akceptowalna. Proszę pamiętać, że czytelność kodu także podlega ocenie.
Jeśli z jakichś powodów nie chciałby Pan lub nie mógł przystąpić do wykonania zadania, bardzo prosimy o przesłanie informacji zwrotnej o takiej decyzji


Zadanie zrealizowałem w Symfony (jako DEBUG zamieszczam) oraz w Django (też jako DEBUG zamieszczam).

Oba pracują na tej samej bazie danych, więc można cokolwiek robić w jednym i drugim, struktury są w zasadzie identyczne.

fragment Unit-testów PHP:

.. code::

   wiks@ubuntu:~/Dokumenty/projects/iai_task/php/iai_invoice$ php bin/phpunit
   PHPUnit 7.5.20 by Sebastian Bergmann and contributors.

   Testing Project Test Suite
   .......                                                             7 / 7 (100%)

   Time: 46 ms, Memory: 6.00 MB

   OK (7 tests, 1022 assertions)


struktuta URL (identyczna jak w Django):

.. code::

   wiks@ubuntu:~/Dokumenty/projects/iai_task/php/iai_invoice$ php bin/console debug:router
    -------------------------- -------- -------- ------ ------------------------------------
     Name                       Method   Scheme   Host   Path
    -------------------------- -------- -------- ------ ------------------------------------
     angular_url                ANY      ANY      ANY    /c/an
     customers_main             ANY      ANY      ANY    /c
     customer_show              ANY      ANY      ANY    /c/s/{customer_id}
     customer_add_edit          ANY      ANY      ANY    /c/e/{customer_id}
     invoices_main              ANY      ANY      ANY    /i
     invoices_list              ANY      ANY      ANY    /i/l
     invoice_add                ANY      ANY      ANY    /i/a/{customer_id}
     invoice_show               ANY      ANY      ANY    /i/s/{invoice_id}
     invoice_edit               ANY      ANY      ANY    /i/e/{invoice_id}
     invoice_add_item_choice    ANY      ANY      ANY    /i/ai/{invoice_id}
     invoice_add_item           ANY      ANY      ANY    /i/ai/{invoice_id}/{item_id}
     invoice_del_item           ANY      ANY      ANY    /i/di/{invoice_id}/{item_id}/{iid}
     invoice_delete             ANY      ANY      ANY    /i/d/{invoice_id}
     items_list                 ANY      ANY      ANY    /t
     index                      ANY      ANY      ANY    /
     myfirm_main                ANY      ANY      ANY    /m
     myfirm_edit                ANY      ANY      ANY    /m/e
    -------------------------- -------- -------- ------ ------------------------------------

   wiks@ubuntu:~/Dokumenty/projects/iai_task/php/iai_invoice$


(kurcze, nie zdążę tutaj zbyt wiele napisać, w każdym razie Sphinx`a też mam opanowanego,
przykład dokumentacji wykonanj w nim: http://aboutloadcounter.qrgo.pl/ )


Co można dodać na tą chwilę (niestety brakło mi czasu):

// todo drukuj do PDF

// todo dodawanie i edycja towarów

// todo klasa z rodzajem jednostek sztuki/kg etc

// todo edycja klasy VAT

// todo DigitValues2words dla innych języków

// todo - dopracuj inne formy przelewu wg ID

// todo testy Selenium (brakło mi czasu)


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
