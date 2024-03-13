#  Utiliser Django-DSFR

## Bien commencer

Pour utiliser Django-DSFR dans votre application après l’installation, vous pouvez commencer à utiliser la balise `{% extends "dsfr/base.html" %}` dans vos [gabarits Django](https://docs.djangoproject.com/fr/5.0/topics/templates/) et mettre votre contenu dans le bloc `{% block content %}{% endblock content %}`.

Vous pouvez faire appel aux [composants du système de design implémentés](/django-dsfr/components/) en appelant la balise `{% load dsfr_tags %}` en haut de vos fichiers.


## Étendre les gabarits de base
Si vous avez besoin d'aller plus loin, vous pouvez étendre `base.html` (et potentiellement `header.html` et `footer.html`).

Vous pouvez prendre exemple sur cette application (cf. [code source](https://github.com/numerique-gouv/django-dsfr/tree/main/example_app))

### Fichier base.html
Dans le répertoire de votre application, créez le ficher `<votre_app>/templates/<votre_app>/base.html` avec le contenu suivant :

```{.django}
<!-- <votre_app>/templates/<votre_app>/base.html -->
{% extends "dsfr/base.html" %}

{% block header %}
  {% include "<votre_app>/blocks/header.html" %}
{% endblock header %}

{% block footer %}
  {% include "<votre_app>/blocks/footer.html" %}
{% endblock footer %}
```

### Fichiers header.hml et footer.hml

Voir la documentation de ces composants :

- [En-tête (header)](/django-dsfr/components/header/)
- [Pied de page (footer)](/django-dsfr/components/footer/)

### Remplacer au lieu d’étendre

Dans le cas où les gabarits fournis se révéleraient trop limités, n’hésitez pas à les remplacer complètement par les vôtres. En plus des composants du Système de design de l’État lui-même, vous pouvez alors utiliser certaines balises pour vous faciliter le travail, notamment :

- [CSS global](/django-dsfr/components/css/)
- [JS global](/django-dsfr/components/js/)
- [Messages Django dans une alerte](/django-dsfr/components/django_messages/)


## Gestion de la configuration en admin

Vous pouvez personnaliser certains éléments du site via une "configuration du site" dans l’[administration de Django](https://docs.djangoproject.com/fr/5.0/ref/contrib/admin/).

Cela permet notamment aux utilisateurs de les modifier sans passer par un développement.

- Ajoutez le `context_processor` au fichier `settings.py` :

```{ .python }
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
```

- Créez un objet "DsfrConfig" dans le panneau d’administration (section Système de design de l’État > Configurations.)
