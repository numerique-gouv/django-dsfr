# Installation de django-DSFR

## Installation basique

- Installez le paquet

```{ .bash }
pip install django-dsfr
```

- Ajoutez `widget_tweaks` et `dsfr` à `INSTALLED_APPS` dans le `settings.py` avant la ou les app avec laquelle vous voulez l’utiliser :

```{ .python }
INSTALLED_APPS = [
    ...
    "widget_tweaks"
    "dsfr",
    <votre_app>
]
```

- Ajouter les lignes suivantes dans la section `TEMPLATES` du `settings.py` pour faire fonctionner les formulaires :

```{ .python }
TEMPLATES = [
    {
        [...]
        "DIRS": [
            os.path.join(BASE_DIR, "dsfr/templates"),
            os.path.join(BASE_DIR, "templates"),
        ],
    },
]
```

- Ajouter le `FORM_RENDERER` in `settings.py` pour faire fonctionner les formulaires :

```{ .python }
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"
```

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
