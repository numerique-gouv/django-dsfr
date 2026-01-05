from django.test import SimpleTestCase
from django.template import Context, Template


class DsfrMdTagTest(SimpleTestCase):
    def test_md_tag_rendered(self):
        context = Context(
            {
                "content": """
# Titre de niveau 1

Contenu *avec* de la **mise en forme** et même un lien vers [la doc de django-dsfr](https://numerique-gouv.github.io/django-dsfr/).

## Titre de niveau 2 affiché comme niveau 6 {: .fr-h6 }

Liste à puces :

- Premier élément ;
- Second élément.

!!! note "Attention !"
    Contenu de la mise en avant

!! note
    Contenu de la mise en exergue

> Texte d’une citation…
qui peut être sur plusieurs lignes.

Jusqu’à la prochaine ligne vide.

| Colonne 1          | Colonne 2          |
|--------------------|--------------------|
| Ligne 1, colonne 1 | Ligne 1, colonne 2 |
| Ligne 2, colonne 1 | Ligne 2, colonne 2 |
                """
            }
        )
        template_to_render = Template("{% load dsfr_md_tags %} {{ content|dsfr_md }}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """<h1>Titre de niveau 1</h1>
            <p>Contenu <em>avec</em> de la <strong>mise en forme</strong> et même un lien vers <a href="https://numerique-gouv.github.io/django-dsfr/" rel="noopener external" target="_blank" title="la doc de django-dsfr - nouvelle fenêtre">la doc de django-dsfr</a>.</p>
            <h2 class="fr-h6">Titre de niveau 2 affiché comme niveau 6</h2>
            <p>Liste à puces :</p>
            <ul>
              <li>Premier élément ;</li>
              <li>Second élément.</li>
            </ul>
            <div class="fr-callout note">
              <p class="fr-callout__title">Attention !</p>
              <p class="fr-callout__text">Contenu de la mise en avant</p>
            </div>
            <div class="fr-highlight note">
              <p>Contenu de la mise en exergue</p>
            </div>
            <figure class="fr-quote">
              <blockquote>
                <p>Texte d’une citation…<br>qui peut être sur plusieurs lignes.</p></blockquote>
            </figure>
            <p>Jusqu’à la prochaine ligne vide.</p>
            <div class="fr-table">
              <div class="fr-table__wrapper">
                <div class="fr-table__container">
                  <div class="fr-table__content">
                    <table>
                      <thead>
                        <tr>
                          <th>Colonne 1</th>
                          <th>Colonne 2</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>Ligne 1, colonne 1</td>
                          <td>Ligne 1, colonne 2</td>
                        </tr>
                        <tr>
                          <td>Ligne 2, colonne 1</td>
                          <td>Ligne 2, colonne 2</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>""",
            rendered_template,
        )
