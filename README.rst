===========
Django-DSFR
===========

Django-DSFR is a Django app to integrate the `French government Design System ("Système de design de l’État français") <https://www.systeme-de-design.gouv.fr/>`_.


This app was created as a part of `Open Collectivités <https://github.com/entrepreneur-interet-general/opencollectivites>`_ and is very much a work in progress. See the `documentation (in French) <https://github.com/entrepreneur-interet-general/django-dsfr/blob/main/DOC.md>`_ for details.

Django-DSFR (partly) implements the `version 1.1.0 of the DSFR <https://gouvfr.atlassian.net/wiki/spaces/DB/pages/806912001/Version+1.1.0>`_.

Requirements
------------
Tested with Python 3.8 and Django 3.2.5. Per `vermin <https://github.com/netromdk/vermin>`_, it should work with Python >= 3.0, and it should work with old versions of Django too.

Quick start
-----------

1. Install with :code:`pip install django-dsfr`.

2. Add "dsfr" to your INSTALLED_APPS setting like this, before the app you want to use it with::

    INSTALLED_APPS = [
        ...
        'dsfr',
        <your_app>
    ]

3. Include the tags in your base.html file::

    # <your_app>/templates/<your_app>/base.html
    {% load static dsfr_tags %}

    <!doctype html>
    <html lang="fr" data-fr-theme="default">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

      {% dsfr_css %}
      {% dsfr_favicon %}

      {% block extra_css %}{% endblock %}

      <title>MyApp</title>
    </head>

    <body>
      <main id="content">
        {% block custom_header %}
          {% include "dsfr/header.html" %}
        {% endblock %}
        {% dsfr_theme_modale %}

        {% block content %}{% endblock %}

        {% include "dsfr/footer.html" %}
      </main>

      {% dsfr_js %}
      {% block extra_js %}{% endblock %}
    </body>

    </html> 

4. Start the development server and visit http://127.0.0.1:8000/
