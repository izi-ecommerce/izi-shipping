# -*- coding: utf-8 -*-
from decimal import Decimal as D

IZI_SHIPPING_WEIGHT_PRECISION = D('0.000')

IZI_SHIPPING_VOLUME_PRECISION = D('0.000') 

# per product defaults
# 0.1m x 0.1m x 0.1m
IZI_SHIPPING_DEFAULT_BOX = {'width': float('0.1'),
                              'height': float('0.1'),
                              'length': float('0.1')}

# 1 Kg 
IZI_SHIPPING_DEFAULT_WEIGHT = 1 

# basket volume * VOLUME_RATIO = estimated container(s) volume
# very simple method
IZI_SHIPPING_VOLUME_RATIO = D('1.3')

# default city of origin to calculate shipping cost via APIs
IZI_SHIPPING_DEFAULT_ORIGIN = u'Санкт-Петербург'

IZI_SHIPPING_API_ENABLED = ['pecom', 'emspost']

# Workaround for javascripted form fields (such as KLADR) which should be cleaned before, e.g. "г. Москва" -> "Москва"
IZI_CITY_PREFIX_SEPARATOR = '. '

# for black and white lists packed in TextField
IZI_SHIPPING_LIST_SEPARATOR = ';'

# allow users to choose city of destination manually if no code found during calculation
IZI_SHIPPING_CHANGE_DESTINATION = True

# is method available or not if no destination's code found for charge calculation
IZI_SHIPPING_IF_NOT_FOUND = True