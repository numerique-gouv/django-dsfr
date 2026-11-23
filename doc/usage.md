# Utilisation

## Bien commencer

Pour utiliser Django-DSFR dans votre application après l’installation, vous
pouvez commencer à utiliser la balise `{% extends "dsfr/base.html" %}` dans
vos [gabarits Django](https://docs.djangoproject.com/fr/5.0/topics/templates/)
et mettre votre contenu dans le bloc `{% block content %}{% endblock content %}`.

Vous pouvez faire appel aux [composants du système de design implémentés](/django-dsfr/components/)
en appelant la balise `{% load dsfr_tags %}` en haut de vos fichiers.

## Étendre les gabarits de base

Si vous avez besoin d'aller plus loin, vous pouvez étendre `base.html`
(et potentiellement `header.html` et `footer.html`).

### Fichier base.html

Dans le répertoire de votre application, créez le ficher `<votre_app>/templates/<votre_app>/base.html`
avec le contenu suivant :

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

Dans le cas où les gabarits fournis se révéleraient trop limités, n’hésitez pas
à les remplacer complètement par les vôtres. En plus des composants du Système
de design de l’État lui-même, vous pouvez alors utiliser certaines balises pour
vous faciliter le travail, notamment :

- [CSS global](/django-dsfr/components/css/)
- [JS global](/django-dsfr/components/js/)
- [Messages Django dans une alerte](/django-dsfr/components/django_messages/)

## Gestion de la configuration en admin

Vous pouvez personnaliser certains éléments du site via une "configuration du site"
dans l’[administration de Django](https://docs.djangoproject.com/fr/5.0/ref/contrib/admin/).

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

## Paramètres (optionnels)

- `DSFR_CHECK_DEPRECATED` (défaut: `False`) : si `True`, vérifie la présence de
    paramètres obsolètes à l’intérieur des template tags
- `DSFR_USE_INTEGRITY_CHECKSUMS`  (défaut: `True`)  : si `True`, intègre des
    checksums d’intégrité sur les fichiers CSS et JS globaux insérés par
    `{% dsfr_css %}` et `{% dsfr_js %}` (voir
    [Checksums d’intégrité](#checksums-dintegrite)).

- Créez un objet "DsfrConfig" dans le panneau d’administration
    (section Système de design de l’État > Configurations.)

## Checksums d’intégrité {: #checksums-dintegrite }

Les checksums d’intégrité ([Subresource Integrity](https://developer.mozilla.org/fr/docs/Web/Security/Subresource_Integrity))
sont calculés à la volée, une seule fois par processus, à partir du fichier
réellement servi :

- avec un stockage qui réécrit les fichiers statiques
    (`ManifestStaticFilesStorage`, `CompressedManifestStaticFilesStorage` de
    Whitenoise, etc.) et `DEBUG = False`, à partir du fichier généré par
    `collectstatic` ;
- sinon, à partir du fichier trouvé par les *finders* de Django, ce qui prend
    en compte un fichier surchargé dans `STATICFILES_DIRS`.

Si le fichier ne peut pas être lu (par exemple si `collectstatic` n’a pas été
lancé), le checksum est omis et un avertissement est journalisé.

Ils sont aussi disponibles pour n’importe quel fichier statique du projet,
dans un gabarit :

```django
{% load static dsfr_tags %}
<link rel="stylesheet"
      href="{% static 'css/site.css' %}"
      integrity="{% dsfr_integrity 'css/site.css' %}">
```

ou en Python :

```python
from dsfr.utils import get_integrity

get_integrity("css/site.css")  # "sha384-…", ou None si le fichier est illisible
```

Le tag renvoie une chaîne vide si le fichier ne peut pas être lu : un attribut
`integrity` vide désactive la vérification. Il ne dépend pas du paramètre
`DSFR_USE_INTEGRITY_CHECKSUMS`.

### Site derrière un proxy ou un CDN (Cloudflare, Imperva…)

Le navigateur vérifie le checksum sur le fichier qu’il reçoit : si un
intermédiaire modifie les fichiers CSS ou JS, ils sont bloqués. Dans ce cas :

- désactivez les optimisations qui réécrivent les fichiers statiques
    (minification, réécriture des scripts comme Rocket Loader chez Cloudflare,
    optimisation de contenu chez Imperva…) ou envoyez l’en-tête
    `Cache-Control: no-transform` sur ces fichiers (avec Whitenoise, via
    `WHITENOISE_ADD_HEADERS_FUNCTION`). La compression (gzip, brotli) ne pose
    pas de problème ;
- privilégiez un stockage avec empreinte dans le nom des fichiers
    (`ManifestStaticFilesStorage`, `CompressedManifestStaticFilesStorage`) :
    sinon, après une mise à jour, le cache peut servir un ancien fichier
    avec un nouveau checksum, et il faut alors purger le cache à chaque
    déploiement ;
- si les fichiers statiques sont servis depuis un autre domaine que les pages,
    le navigateur exige l’attribut `crossorigin` et des en-têtes CORS pour
    vérifier le checksum, ce que les gabarits `{% dsfr_css %}` et
    `{% dsfr_js %}` ne gèrent pas actuellement.

Si une de ces conditions ne peut pas être remplie, désactivez les checksums
avec `DSFR_USE_INTEGRITY_CHECKSUMS = False`. En cas de problème, la console du
navigateur affiche une erreur du type
`Failed to find a valid digest in the 'integrity' attribute`.

### Module `dsfr.checksums` (obsolète)

Le module `dsfr.checksums` (`INTEGRITY_CSS`, `INTEGRITY_UTILITY_CSS`,
`INTEGRITY_JS_MODULE`, `INTEGRITY_JS_NOMODULE`) est obsolète : ses valeurs
sont désormais calculées de la même manière et son utilisation émet un
`DeprecationWarning`. Il sera supprimé dans une prochaine version majeure.

## Application d’exemple

Vous pouvez prendre exemple sur cette application (cf. [code source](https://github.com/numerique-gouv/django-dsfr/tree/main/example_app)).

Elle consiste en un générateur pour la présente documentation. Dans la mesure
où celle-ci est hébergée de manière statique, un export est fait automatiquement
via [Django-distill](https://github.com/meeb/django-distill).
