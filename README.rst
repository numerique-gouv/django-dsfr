.. image:: https://img.shields.io/github/v/release/numerique-gouv/django-dsfr.svg
    :target: https://github.com/numerique-gouv/django-dsfr/releases/
.. image:: https://badge.fury.io/py/django-dsfr.svg
    :target: https://pypi.org/project/django-dsfr/

.. image:: https://github.com/numerique-gouv/django-dsfr/actions/workflows/ci-3-8.yml/badge.svg
    :target: https://github.com/numerique-gouv/django-dsfr/actions/workflows/ci-3-8.yml
.. image:: https://github.com/numerique-gouv/django-dsfr/actions/workflows/ci-3-10.yml/badge.svg
    :target: https://github.com/numerique-gouv/django-dsfr/actions/workflows/ci-3-10.yml

.. image:: https://github.com/numerique-gouv/django-dsfr/actions/workflows/codeql-analysis.yml/badge.svg
    :target: https://github.com/numerique-gouv/django-dsfr/actions/workflows/codeql-analysis.yml
.. image:: https://img.shields.io/badge/security-bandit-yellow.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security Status

===========
Django-DSFR
===========

Django-DSFR is a Django app to integrate the `French government Design System ("Système de design de l’État français") <https://www.systeme-de-design.gouv.fr/>`_.

Documentation
-------------

See the `documentation (in French) <https://numerique-gouv.github.io/django-dsfr/>`_ for details.

Django-DSFR implements the `version 1.12.1 of the DSFR <https://www.systeme-de-design.gouv.fr/a-propos/versions/version-courante>`_ (see also the `Github releases page <https://github.com/GouvernementFR/dsfr/releases/>`_)

Requirements
------------
Tested with Python 3.8 to 3.12 and Django 3.2 to 5.0. Per `vermin <https://github.com/netromdk/vermin>`_, it should work with Python >= 3.6, and it should work with old versions of Django too.

Note: Only supported versions of Django and Python are supported by this project. You can check the supported versions and their end of life on the following pages:

- `Python <https://devguide.python.org/versions/>`_
- `Django <https://www.djangoproject.com/download/#supported-versions>`_

Warning: Support for Django < 4.0 and Python < 3.10 will be removed at the end of 2024.

Quick start
-----------

See the `INSTALL.md <INSTALL.md>`_ file.

History
-------
This app was originally created as a part of `Open Collectivités <https://github.com/entrepreneur-interet-general/opencollectivites>`_ in 2020, and then maintained as part of `Aides-territoires <https://github.com/MTES-MCT/aides-territoires>`_ in 2022-2023.

It is now maintained as part of `@numerique-gouv <https://github.com/numerique-gouv>`_ alongside the Wagtail-based `Sites faciles <https://github.com/numerique-gouv/sites-faciles>`_.
