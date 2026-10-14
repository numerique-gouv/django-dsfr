from django.template import Context, Template
from django.test import SimpleTestCase, override_settings


class DsfrMdTagTest(SimpleTestCase):
    def test_md_tag_rendered(self):
        context = Context({"content": """
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
                """})
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

    def test_strips_inline_js(self):
        context = Context({"content": """# Titre {: onclick="alert()" }"""})
        template_to_render = Template("{% load dsfr_md_tags %} {{ content|dsfr_md }}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML("<h1>Titre</h1>", rendered_template)

    def test_md_tag_with_toc_rendered(self):
        context = Context({"content": """[TOC]
# Titre de niveau 1

Contenu niveau 1

## Titre de niveau 2

Contenu niveau 2

# Titre de niveau 1 à nouveau

Contenu
                """})
        template_to_render = Template(
            "{% load dsfr_md_tags %} {{ content|dsfr_md_with_toc }}"
        )
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """<nav aria-labelledby="fr-summary-title" class="fr-summary" role="navigation">
            <h2 class="fr-summary__title" id="fr-summary-title">Sommaire</h2>
            <ol>
              <li>
                <a class="fr-summary__link" href="#titre-de-niveau-1">Titre de niveau 1</a>
                <ol>
                  <li><a class="fr-summary__link" href="#titre-de-niveau-2">Titre de niveau 2</a></li>
                </ol>
              </li>
              <li>
                <a class="fr-summary__link" href="#titre-de-niveau-1-a-nouveau">Titre de niveau 1 à nouveau</a>
              </li>
            </ol>
            </nav>
            """,
            rendered_template,
        )


class DsfrMdEmojiTest(SimpleTestCase):
    def render(self, content, md_filter="dsfr_md"):
        return Template(
            "{% load dsfr_tags dsfr_md_tags %}"
            f"{{{{ content|{md_filter}|dsfr_emoji }}}}"
        ).render(Context({"content": content}))

    def span(self, emoji):
        return f'<span aria-hidden="true">{emoji}</span>'

    def test_md_alone_does_not_wrap_emojis(self):
        rendered_template = Template(
            "{% load dsfr_md_tags %}{{ content|dsfr_md }}"
        ).render(Context({"content": "Texte 😬"}))
        self.assertInHTML("<p>Texte 😬</p>", rendered_template)

    def test_emojis_in_text_are_wrapped(self):
        rendered_template = self.render("# Titre 🎉\n\nTexte 😬 et **gras 👍🏽**")
        self.assertInHTML(f"<h1>Titre {self.span('🎉')}</h1>", rendered_template)
        self.assertInHTML(
            f"<p>Texte {self.span('😬')} et <strong>gras {self.span('👍🏽')}</strong></p>",
            rendered_template,
        )

    def test_emojis_in_lists_and_quotes_are_wrapped(self):
        rendered_template = self.render("- Élément 🇫🇷\n\n> Citation 👨‍👩‍👧")
        self.assertInHTML(
            f"<ul><li>Élément {self.span('🇫🇷')}</li></ul>", rendered_template
        )
        self.assertIn(f"Citation {self.span('👨‍👩‍👧')}", rendered_template)

    def test_emojis_in_attributes_are_not_wrapped(self):
        rendered_template = self.render(
            '![Logo 🇫🇷](/img.png "Titre 🎉")\n\n[Lien 😬](https://example.com)'
        )
        self.assertIn('alt="Logo 🇫🇷"', rendered_template)
        self.assertIn('title="Titre 🎉"', rendered_template)
        self.assertIn('title="Lien 😬 - nouvelle fenêtre"', rendered_template)
        self.assertIn(f"Lien {self.span('😬')}</a>", rendered_template)

    def test_emojis_with_toc_are_wrapped(self):
        rendered_template = self.render(
            "[TOC]\n# Titre 🎉\n\nTexte", "dsfr_md_with_toc"
        )
        self.assertInHTML(
            f'<a class="fr-summary__link" href="#titre">Titre {self.span("🎉")}</a>',
            rendered_template,
        )
        self.assertInHTML(
            f'<h1 id="titre">Titre {self.span("🎉")}</h1>', rendered_template
        )

    def test_emojis_in_code_are_not_wrapped(self):
        rendered_template = self.render("Code `😬` ici 🎉\n\n    bloc 👍\n")
        self.assertInHTML(
            f"<p>Code <code>😬</code> ici {self.span('🎉')}</p>", rendered_template
        )
        self.assertInHTML("<pre><code>bloc 👍\n</code></pre>", rendered_template)

    @override_settings(DSFR_WRAP_EMOJIS=False)
    def test_setting_disables_wrapping(self):
        self.assertInHTML("<p>Texte 😬</p>", self.render("Texte 😬"))
