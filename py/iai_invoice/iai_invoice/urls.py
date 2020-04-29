# -*- coding: utf8 -*-

"""iai_invoice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from myfirm import views as myfirm_views
from invoices import views as invoices_views

urlpatterns = [
    path('', myfirm_views.index, name='index'),
    path('i/', include('invoices.urls')),
    path('t/', include('items.urls')),
    path('m/', include('myfirm.urls')),
    path('c/', include('customers.urls')),
    path('admin/', admin.site.urls),
]
