.. image:: https://badge.fury.io/py/django-dsfr.svg
    :target: https://pypi.org/project/django-dsfr/

.. image:: https://github.com/entrepreneur-interet-general/django-dsfr/actions/workflows/django.yml/badge.svg
    :target: https://github.com/entrepreneur-interet-general/django-dsfr/actions/workflows/django.yml

.. image:: https://github.com/entrepreneur-interet-general/django-dsfr/actions/workflows/codeql-analysis.yml/badge.svg
    :target: https://github.com/entrepreneur-interet-general/django-dsfr/actions/workflows/codeql-analysis.yml


===========
Django-DSFR
===========

Django-DSFR is a Django app to integrate the `French government Design System ("Système de design de l’État français") <https://www.systeme-de-design.gouv.fr/>`_.


This app was created as a part of `Open Collectivités <https://github.com/entrepreneur-interet-general/opencollectivites>`_ and is very much a work in progress. See the `documentation (in French) <https://entrepreneur-interet-general.github.io/django-dsfr/>`_ for details.

Django-DSFR (partly) implements the `version 1.8.5 of the DSFR <https://www.systeme-de-design.gouv.fr/a-propos/versions-du-dsfr/version-courante>`_.

Requirements
------------
Tested with Python 3.7 to 3.10 and Django 3.2.5 to 4.1.16. Per `vermin <https://github.com/netromdk/vermin>`_, it should work with Python >= 3.0, and it should work with old versions of Django too.

Quick start
-----------

1. Install with :code:`pip install django-dsfr`.

2. Add "widget_tweaks" and "dsfr" to INSTALLED_APPS in your settings.py like this, before the app you want to use it with::

    INSTALLED_APPS = [
        ...
        "widget_tweaks"
        "dsfr",
        <your_app>
    ]

3. Add the following info in the TEMPLATES section in your settings.py so that the choice forms work::

    TEMPLATES = [
        {        
            [...]
            "DIRS": [
                os.path.join(BASE_DIR, "dsfr/templates"),
                os.path.join(BASE_DIR, "templates"),
            ],
        },
    ]

4. Add the following FORM_RENDERER in settings.py so that the choice forms work::

    FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

5. (Optional) Add the context processor to your settings.py and create an instance of "DsfrConfig" in the admin panel::

    TEMPLATES = [
        {
            [...]
            "OPTIONS": {
                "context_processors": [
                    [...]
                    "dsfr.context_processors.site_config",
                ],
            },
        },
    ]

6. Include the tags in your base.html file (see example file at https://github.com/entrepreneur-interet-general/django-dsfr/blob/main/example_app/templates/example_app/base.html)

7. Start the development server and visit http://127.0.0.1:8000/