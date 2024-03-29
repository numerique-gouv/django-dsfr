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
- Sélecteur de langue (translate) : ([Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/selecteur-de-langue) — [Exemple](https://main--ds-gouv.netlify.app/example/component/translate/)), à insérer dans le bloc `header_tools`.


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
