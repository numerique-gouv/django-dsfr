L’en-tête est géré grâce à une balise `include` dans le fichier `base.html`. Si vous n’avez pas besoin de le personnaliser, vous n’avez rien à faire.

Il est alors possible de personnaliser le titre, le sous-titre, ainsi que le bloc-marque, via la configuration du site dans l’administration de Django.

- <a class="fr-link fr-icon-external-link-line fr-link--icon-right fr-link--lg" href="https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/en-tete" target="_blank" rel="noopener noreferrer">
        Voir la page de documentation du composant sur le Système de Design de l’État
        <span class="fr-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>
- <a class="fr-link fr-icon-external-link-line fr-link--icon-right fr-link--lg" href="https://main--ds-gouv.netlify.app/example/component/header/" target="_blank" rel="noopener noreferrer">
        Voir la page d’exemple du Système de Design de l’État
        <span class="fr-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>

## Composants liés
Le gabarit d’en-tête est également l’endroit où inclure les composants suivants :

- Navigation principale (navigation) ([Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/navigation-principale) — [Exemple](https://main--ds-gouv.netlify.app/example/component/navigation/)), à insérer dans le bloc `main_menu`.
- Sélecteur de langue (translate) : ([Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/selecteur-de-langue) — [Exemple](https://main--ds-gouv.netlify.app/example/component/translate/)), à insérer dans le bloc `header_tools`. L’application d’exemple donne un exemple d’implémentation ne traduisant que l’interface, et ne changeant pas l’URL, mais il est plutôt recommandé de définir un préfixe de langue dans l’URL, cf. la [documentation de Django](https://docs.djangoproject.com/fr/5.0/topics/i18n/translation/).

## Personnaliser

Il est possible de l’étendre pour le personnaliser, par exemple pour ajouter la barre de recherche :

```{.django}
<!-- <votre_app>/templates/<votre_app>/base.html -->
{% extends "dsfr/base.html" %}

<!-- [...] -->
{% block header %}
  {% include "<votre_app>/blocks/header.html" %}
{% endblock header %}

```

```
<!-- <votre_app>/templates/<votre_app>/blocks/header.html -->
{% extends "dsfr/header.html" %}

{% block header_search %}
  <div class="fr-header__search fr-modal" id="modal-search">
    <div class="fr-container fr-container-lg--fluid">
      <button class="fr-btn--close fr-btn"
              aria-controls="modal-search"
              title="Fermer">
        Fermer
      </button>
      <form action="{% url 'page_search' %}" method="get">
        <div class="fr-search-bar" id="search-bar" role="search">
          <label class="fr-label" for="search-bar-input">
            Rechercher
          </label>
          <input class="fr-input"
                 placeholder="Rechercher"
                 type="search"
                 id="query"
                 name="q">
          <button class="fr-btn" title="Rechercher">
            Rechercher
          </button>
        </div>
      </form>
    </div>
  </div>
{% endblock header_search %}
```

## Opengraph

Un bloc `opengraph`, vide par défaut, est fourni pour permettre d’entrer des données de partage sur les réseaux sociaux.


```{.django}
<!-- <votre_app>/templates/<votre_app>/base.html -->
{% extends "dsfr/base.html" %}

<!-- [...] -->
{% block opengraph }
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="[À MODIFIER - @usernameTwitter]">
  <meta property="og:title" content="[À MODIFIER - Système de Design de l'État]">
  <meta property="og:description" content="[À MODIFIER - Développer vos sites et applications en utilisant des composants prêts à l'emploi, accessibles et ergonomiques]">
  <meta property="og:image" content="[À MODIFIER - https://systeme-de-design.gouv.fr/src/img/systeme-de-design.gouv.fr.jpg]">
  <meta property="og:type" content="website">
  <meta property="og:url" content="[À MODIFIER - https://systeme-de-design.gouv.fr/]">
  <meta property="og:site_name" content="[À MODIFIER - Site officiel du Système de Design de l'État]">
  <meta property="og:image:alt" content="[À MODIFIER - République Française - Système de Design de l'État]">
  <meta name="twitter:image:alt" content="[À MODIFIER - République Française - Système de Design de l'État]">
{% endblock opengraph }
```
