# Installation de Django-DSFR

## Installation basique

- Installez le paquet

```{ .bash }
pip install django-dsfr
```
### Pour Django 5.0+

- Ajoutez `widget_tweaks` et `dsfr` à `INSTALLED_APPS` dans le `settings.py` avant la ou les app avec laquelle vous voulez l’utiliser :

```{ .python }
INSTALLED_APPS = [
    ...
    "widget_tweaks",
    "dsfr",
    <votre_app>
]
```

### Pour Django 4.2 et avant

- Ajoutez `widget_tweaks`, `dsfr` et `django.forms` à `INSTALLED_APPS` dans le `settings.py` avant la ou les app avec laquelle vous voulez l’utiliser :

```{ .python }
INSTALLED_APPS = [
    ...
    "widget_tweaks",
    "dsfr",
    "django.forms",
    <votre_app>
]
```

**Attention** : si `django.forms` apparait déjà dans `INSTALLED_APPS`, il doit être placé *après* `dsfr`. Sinon les `FormSet`s ne seront pas correctement rendus.

- Ajouter le `FORM_RENDERER` in `settings.py` pour faire fonctionner les formulaires :

```{ .python }
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"
```

### Pour toutes les versions

- Inclure les tags dans votre fichier `base.html` (voir par exemple sur [base.html](https://github.com/numerique-gouv/django-dsfr/blob/main/example_app/templates/example_app/base.html))

- Lancer le serveur (`python manage.py runserver`) et aller sur [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Paramètres optionnels
À ajouter dans le fichier `settings.py` de votre projet :

- `DSFR_CHECK_DEPRECATED_PARAMS` (defaut: False)

Si valeur à `True`, permet d’avoir des avertissements dans la console si on utilise des valeurs obsolètes pour les paramètres des `templatetags`.

Les tags obsolètes feront toujours l’objet d’un avertissement.
