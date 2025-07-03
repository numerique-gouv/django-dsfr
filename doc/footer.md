Le pied de page est géré grâce à une balise `include` dans le fichier `base.html`. Si vous n’avez pas besoin de le personnaliser, vous n’avez rien à faire.

Il est alors possible de personnaliser la description ainsi que le bloc-marque via la configuration du site dans l’administration de Django.


- <a class="fr-link fr-icon-external-link-line fr-link--icon-right fr-link--lg" href="https://www.systeme-de-design.gouv.fr/version-courante/fr/composants/pied-de-page" target="_blank" rel="noopener noreferrer">
        Voir la page de documentation du composant sur le Système de Design de l’État
        <span class="fr-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>
- <a class="fr-link fr-icon-external-link-line fr-link--icon-right fr-link--lg" href="https://main--ds-gouv.netlify.app/example/component/footer/" target="_blank" rel="noopener noreferrer">
        Voir la page d’exemple du Système de Design de l’État
        <span class="fr-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>
- <a class="fr-link fr-icon-external-link-line fr-link--icon-right fr-link--lg" href="https://storybook.systeme-de-design.gouv.fr/?path=/docs/footer--docs" target="_blank" rel="noopener noreferrer">
        Voir la page du composant sur Storybook
        <span class="fr-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>

## Personnaliser

Il est possible de l’étendre pour le personnaliser, par exemple pour ajouter le sélecteur de thème :

```{.django}
<!-- <votre_app>/templates/<votre_app>/base.html -->
{% extends "dsfr/base.html" %}

<!-- [...] -->
{% block footer %}
  {% include "<votre_app>/blocks/footer.html" %}
{% endblock footer %}

```

```
<!-- <votre_app>/templates/<votre_app>/blocks/footer.html -->
{% extends "dsfr/footer.html" %}
{% block footer_links %}
  {{ block.super }}
  <li class="fr-footer__bottom-item">
    <button id="footer__bottom-link__parametres-affichage"
            aria-controls="fr-theme-modal"
            data-fr-opened="false"
            class="fr-icon-theme-fill fr-link--icon-left fr-footer__bottom-link"
            data-fr-js-modal-button="true">
      Paramètres d’affichage
    </button>
  </li>
{% endblock footer_links %}
```

## Blocs dépréciés
- Le bloc `brand`, qui ne permet pas toutes les personnalisations nécessaires, va être supprimé à terme. Les personnalisations sont à mettre dans le nouveau bloc `footer_brand`.
- Même chose pour le bloc `footer_content`, à remplacer à terme par le nouveau bloc `footer_description`.
