=============================
django-izi-shipping
=============================

.. image:: https://travis-ci.org/okfish/django-izi-shipping.png?branch=master
    :target: https://travis-ci.org/okfish/django-izi-shipping

.. image:: https://coveralls.io/repos/okfish/django-izi-shipping/badge.png?branch=master
    :target: https://coveralls.io/r/okfish/django-izi-shipping?branch=master


API-based shipping app for the IZI Ecommerce project. 
Supports APIs for some post services and companies, such as EMS Russian Post, PEC(Pervaya Ekspeditsionnaya), DHL etc.



Documentation
-------------

The full documentation will be available soon at https://django-izi-shipping.readthedocs.org.

Quickstart
----------

Install django-izi-shipping::

    pip install -e git+https://github.com/okfish/django-izi-shipping/django-izi-shipping.git#egg=dajngo-izi-shipping

then add 'izi_shipping' to the INSTALLED_APPS. From now you can override IZI's shipping app
using izi_shipping within your project

e.g.::

#apps/shipping/methods.py

from izi_shipping.methods import SelfPickup

#apps/shipping/repository.py

from izi.apps.shipping import repository

from .methods import * 
from . import models

# Override shipping repository in order to provide our own
# custom methods
class Repository(repository.Repository):
    
    def get_available_shipping_methods(self, basket, user=None, shipping_addr=None, request=None, **kwargs):
        methods = [SelfPickup(),]
        #...
        methods.extend(list(models.ShippingCompany.objects.all().filter(is_active=True)))
        return methods

#apps/shipping/models.py

from izi.apps.shipping import abstract_models
from izi_shipping.models import * 

#... your methods goes here

from izi.apps.shipping.models import *

#apps/shipping/admin.py

from izi_shipping.admin import *
from izi.apps.shipping.admin import *

Dependencies
------------

Install pecomsdk if you would like enable pecom shipping facade::

	pip install -e git+https://github.com/okfish/pecomsdk/pecomsdk.git#egg=pecomsdk

Install py-emspost-api if you would like enable ems shipping facade::

	pip install -e git+https://github.com/okfish/py-emspost-api/py-emspost-api.git#egg=py-emspost-api


Features
--------
* SelfPickup() shipping method. Simply inherited from methods.Free and renamed.
* Easy customisable facades for different APIs
* Facade to the Russian Post EMS using py-emspost-api package
* Facade to the PEC (Pervaya Ekspeditsionnaya Kompania) using pecomsdk package
* Models for shipping companies and containers for packing and shipping cost calculation 
* Packer module assumes Bin Packing Problem can be solved in different ways: using own algorithms or via external APIs

* TODO
