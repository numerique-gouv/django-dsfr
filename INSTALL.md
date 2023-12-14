# Installation de django-DSFR

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
    "widget_tweaks"
    "dsfr",
    <votre_app>
]
```

### Pour Django 4.2 et avant

- Ajoutez `widget_tweaks`, `dsfr` et `django.forms` à `INSTALLED_APPS` dans le `settings.py` avant la ou les app avec laquelle vous voulez l’utiliser :

```{ .python }
INSTALLED_APPS = [
    ...
    "widget_tweaks"
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


## Installation avancée (optionnelle)
### Utilisation de la conf en admin
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

- Créez un objet "DsfrConfig" dans le panneau d’administration
