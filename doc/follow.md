Le bandeau de Lettre d’information et Réseaux Sociaux est géré grâce à une balise `include` à insérer dans le bloc `follow_newsletter_social_media` dans le fichier `base.html`.

```{.django}
<!-- <votre_app>/templates/<votre_app>/base.html -->
{% extends "dsfr/base.html" %}

<!-- [...] -->
{% block follow_newsletter_social_media %}
  <aside role="complementary">
    {% include "dsfr/follow.html" %}
  </aside>
{% endblock follow_newsletter_social_media %}
```

Il est alors possible de personnaliser la description de la lettre d’information, l’URL d’inscription ainsi que les réseaux sociaux via la configuration du site dans l’administration de Django.
`
- `<a class="fr-link fr-icon-external-link-line fr-link--icon-right fr-link--lg" href="https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/pied-de-page" target="_blank" rel="noopener noreferrer">
        Voir la page de documentation du composant sur le Système de Design de l’État
        <span class="fr-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>`
- `<a class="fr-link fr-icon-external-link-line fr-link--icon-right fr-link--lg" href="https://main--ds-gouv.netlify.app/example/component/footer/" target="_blank" rel="noopener noreferrer">
        Voir la page d’exemple du Système de Design de l’État
        <span class="fr-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>

## Classes pour les boutons des réseaux sociaux

- `fr-btn--dailymotion`
- `fr-btn--facebook`
- `fr-btn--github`
- `fr-btn--instagram`
- `fr-btn--linkedin`
- `fr-btn--mastodon`
- `fr-btn--snapchat`
- `fr-btn--telegram`
- `fr-btn--threads`
- `fr-btn--tiktok`
- `fr-btn--twitch`
- `fr-btn--twitter`
- `fr-btn--twitter-x`
- `fr-btn--vimeo`
- `fr-btn--youtube`

## Personnaliser
Il est possible de le remplacer par votre propre bloc pour étendre ses capacités (par exemple pour n’afficher qu’un des deux blocs ou pour inclure le champ d’adhésion directement dans le bandeau.)

```{.django}
<!-- <votre_app>/templates/<votre_app>/base.html -->
{% extends "dsfr/base.html" %}

<!-- [...] -->
{% block follow_newsletter_social_media %}
  {% include "<votre_app>/blocks/follow.html" %}
{% endblock follow_newsletter_social_media %}

```

```{.django}
<!-- <votre_app>/templates/<votre_app>/blocks/follow.html -->
{% extends "dsfr/follow.html" %}
{% block follow_newsletter %}
  <div class="fr-col-12">
      <div class="fr-follow__newsletter">
          <div>
              <h2 class="fr-h5">Abonnez-vous à notre lettre d’information</h2>
              <p class="fr-text--sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
          </div>
          <div>
              <form action="">
                  <div class="fr-input-group">
                      <label class="fr-label" for="newsletter-email">
                          Votre adresse électronique (ex. : nom@domaine.fr)
                      </label>
                      <div class="fr-input-wrap fr-input-wrap--addon">
                          <input class="fr-input" title="Votre adresse électronique (ex. : nom@domaine.fr)" autocomplete="email" attributes="[object Object]" aria-describedby="newsletter-email-hint-text newsletter-email-messages" placeholder="Votre adresse électronique (ex. : nom@domaine.fr)" id="newsletter-email" type="email">
                          <button class="fr-btn" id="newsletter-button" title="S’abonner à notre lettre d’information" type="submit">
                              S’abonner
                          </button>
                      </div>
                      <div class="fr-messages-group" id="newsletter-email-messages" aria-live="assertive">
                      </div>
                  </div>
                  <p id="newsletter-email-hint-text" class="fr-hint-text">En renseignant votre adresse électronique, vous acceptez de recevoir nos actualités par courriel. Vous pouvez vous désinscrire à tout moment à l’aide des liens de désinscription ou en nous contactant.</p>
              </form>
          </div>
      </div>
  </div>
{% endblock follow_newsletter %}

{% block follow_social %}
{% endblock follow_social %}
```
