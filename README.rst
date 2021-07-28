====
DSFR
====

DSFR is a Django app to integrate the `French government Design System ("Système de design de l’État français") <https://www.systeme-de-design.gouv.fr/>`_.

Requirements
------------
Tested with Python 3.8 and Django 3.2.5. Per `vermin <https://github.com/netromdk/vermin>`_, it should work with Python >= 3.0, and it should work with old versions of Django too.

Quick start
-----------

1. Add "dsfr" to your INSTALLED_APPS setting like this, before the app you want to use it with::

    INSTALLED_APPS = [
        ...
        'dsfr',
        <your_app>
    ]

2. Include the tags in your base.html file::

    # <your_app>/templates/<your_app>/base.html
    {% load static %}
    {% load dsfr_tags %}

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
          {% include "core/blocks/header.html" %}
        {% endblock %}
        {% dsfr_theme_modale %}

        {% block content %}{% endblock %}

        {% include "core/blocks/footer_categories.html" %}
        {% include "core/blocks/footer.html" %}
      </main>

      {% dsfr_js %}
      {% block extra_js %}{% endblock %}
    </body>

    </html> 

3. Start the development server and visit http://127.0.0.1:8000/