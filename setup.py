#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import izi_shipping

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = izi_shipping.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='izi-shipping',
    version=version,
    description="""Shipping app for IZI Ecommerce projects. Supports APIs for some post services and companies, such as EMS Vietnam Post, PEC etc.""",
    long_description=readme + '\n\n' + history,
    author='Daniel Do',
    author_email='dotiendiep@gmail.com',
    url='https://github.com/izi-ecommerce/izi-shipping',
    packages=[
        'izi_shipping',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-izi-shipping',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
