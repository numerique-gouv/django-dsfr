from django.test import SimpleTestCase
from django.template import Context, Template
from unittest.mock import MagicMock

from dsfr.checksums import (
    INTEGRITY_CSS,
    INTEGRITY_JS_MODULE,
    INTEGRITY_JS_NOMODULE,
)
from dsfr.templatetags.dsfr_tags import concatenate, hyphenate


class DsfrCssTagTest(SimpleTestCase):
    def test_css_tag_rendered(self):
        context = Context()
        template_to_render = Template("{% load dsfr_tags %} {% dsfr_css %}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            f'<link rel="stylesheet" href="/django-dsfr/static/dsfr/dist/dsfr/dsfr.min.css"  integrity="{ INTEGRITY_CSS }">',  # noqa
            rendered_template,
        )


class DsfrJsTagTest(SimpleTestCase):
    def test_js_tag_rendered(self):
        context = Context()
        template_to_render = Template("{% load dsfr_tags %} {% dsfr_js %}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            f"""
            <script type="module" src="/django-dsfr/static/dsfr/dist/dsfr/dsfr.module.min.js" integrity="{ INTEGRITY_JS_MODULE }"></script>
            <script nomodule src="/django-dsfr/static/dsfr/dist/dsfr/dsfr.nomodule.min.js" integrity="{ INTEGRITY_JS_NOMODULE }"></script>
            """,  # noqa
            rendered_template,
        )


class DsfrJsTagWithNonceTest(SimpleTestCase):
    def test_js_tag_rendered(self):
        context = Context()
        template_to_render = Template(
            "{% load dsfr_tags %} {% dsfr_js nonce='random-nonce' %}"
        )
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            f"""
            <script type="module" src="/django-dsfr/static/dsfr/dist/dsfr/dsfr.module.min.js" integrity="{ INTEGRITY_JS_MODULE }" nonce="random-nonce"></script>
            <script nomodule src="/django-dsfr/static/dsfr/dist/dsfr/dsfr.nomodule.min.js" integrity="{ INTEGRITY_JS_NOMODULE }" nonce="random-nonce"></script>
            """,  # noqa
            rendered_template,
        )


class DsfrFaviconTagTest(SimpleTestCase):
    def test_favicon_tag_rendered(self):
        context = Context()
        template_to_render = Template("{% load dsfr_tags %} {% dsfr_favicon %}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """
            <link rel="apple-touch-icon" href="/django-dsfr/static/dsfr/dist/favicon/apple-touch-icon.png"  /><!-- 180×180 -->
            <link rel="icon" href="/django-dsfr/static/dsfr/dist/favicon/favicon.svg" type="image/svg+xml" />
            <link rel="shortcut icon" href="/django-dsfr/static/dsfr/dist/favicon/favicon.ico" type="image/x-icon" />
            <!-- 32×32 -->
            <link rel="manifest" href="/django-dsfr/static/dsfr/dist/favicon/manifest.webmanifest"
            crossorigin="use-credentials" />
            """,
            rendered_template,
        )


class DsfrThemeModaleTagTest(SimpleTestCase):
    def test_theme_modale_tag_rendered(self):
        context = Context()
        template_to_render = Template("{% load dsfr_tags %} {% dsfr_theme_modale %}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """
            <h1 id="fr-theme-modal-title" class="fr-modal__title">
                Paramètres d’affichage
            </h1>
            """,
            rendered_template,
        )


class DsfrAccordionTagTest(SimpleTestCase):
    test_data = {
        "id": "sample-accordion",
        "title": "Title of the accordion item",
        "content": "<p><b>Bold</b> and <em>emphatic</em> Example content</p>",
    }

    context = Context({"test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_accordion test_data %}")

    def test_accordion_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <section class="fr-accordion">
                <h3 class="fr-accordion__title">
                    <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="sample-accordion">Title of the accordion item</button>
                </h3>
                <div class="fr-collapse" id="sample-accordion">
                    <p><b>Bold</b> and <em>emphatic</em> Example content</p>
                </div>
            </section>
            """,  # noqa
            rendered_template,
        )


class DsfrAccordionGroupTagTest(SimpleTestCase):
    test_data = [
        {
            "id": "sample-accordion",
            "title": "Title of the accordion item",
            "content": "<p><b>Bold</b> and <em>emphatic</em> Example content</p>",
        },
        {
            "id": "sample-accordion-2",
            "title": "Title of the second accordion item",
            "content": "<p><b>Bold</b> and <em>emphatic</em> Example content</p>",
        },
        {
            "id": "sample-accordion-3",
            "title": "Title of the third accordion item",
            "content": "<p><b>Bold</b> and <em>emphatic</em> Example content</p>",
        },
    ]

    context = Context({"test_data": test_data})
    template_to_render = Template(
        "{% load dsfr_tags %} {% dsfr_accordion_group test_data %}"
    )

    def test_accordion_group_count(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """<p><b>Bold</b> and <em>emphatic</em> Example content</p>""",
            rendered_template,
            count=3,
        )


class DsfrAlertTagTest(SimpleTestCase):
    test_data = {
        "title": "Sample title",
        "type": "info",
        "content": "Sample content",
        "heading_tag": "h3",
        "is_collapsible": True,
        "id": "test-alert-message",
    }

    context = Context({"test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_alert test_data %}")

    def test_alert_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML("""<p>Sample content</p>""", rendered_template)

    def test_alert_tag_heading_can_be_set(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """<h3 class="fr-alert__title">Sample title</h3>""", rendered_template
        )

    def test_alert_tag_has_collapse_button(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <button class="fr-btn--close fr-btn" title="Masquer le message" onclick="const alert = this.parentNode; alert.parentNode.removeChild(alert);">
              Masquer le message
            </button>
            """,  # noqa
            rendered_template,
        )

    def test_alert_tag_has_custom_attrs(self):
        test_data = self.test_data.copy()
        test_data.pop("is_collapsible", None)
        test_data["collapsible_attrs"] = {
            "data-controller": "close",
            "data-action": "close#onClick",
        }
        rendered_template = self.template_to_render.render(
            Context({"test_data": test_data})
        )
        self.assertInHTML(
            """
            <button class="fr-btn--close fr-btn" title="Masquer le message" data-controller="close" data-action="close#onClick">
              Masquer le message
            </button>
            """,  # noqa
            rendered_template,
        )


class DsfrBadgeTagTest(SimpleTestCase):
    test_data = {
        "label": "badge label",
        "extra_classes": "fr-badge--success",
    }

    context = Context({"test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_badge test_data %}")

    def test_badge_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <p class="fr-badge fr-badge--success">badge label</p>
            """,
            rendered_template,
        )


class DsfrBreadcrumbTagTest(SimpleTestCase):
    breadcrumb_data = {
        "links": [{"url": "test-url", "title": "Test title"}],
        "current": "Test page",
    }

    context = Context({"breadcrumb_data": breadcrumb_data})
    template_to_render = Template(
        "{% load dsfr_tags %} {% dsfr_breadcrumb breadcrumb_data %}"
    )

    def test_breadcrumb_tag_current_page(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """<a class="fr-breadcrumb__link" aria-current="page">Test page</a>""",
            rendered_template,
        )

    def test_breadcrumb_tag_middle_link(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """<a class="fr-breadcrumb__link" href="test-url">Test title</a>""",
            rendered_template,
        )


class DsfrButtonTagTest(SimpleTestCase):
    test_data = {
        "onclick": "alert('test button action')",
        "label": "button label",
        "type": "button",
        "name": "test-button",
        "extra_classes": "fr-btn--secondary",
    }

    context = Context({"test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_button test_data %}")

    def test_button_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <button
            class="fr-btn fr-btn--secondary"
            onclick="alert(&#x27;test button action&#x27;)"
            type="button"
            name="test-button"
            >
                button label
            </button>
            """,
            rendered_template,
        )


class DsfrButtonGroupTagTest(SimpleTestCase):
    test_data = {
        "extra_classes": "fr-btns-group--equisized",
        "items": [
            {
                "onclick": "alert('test button action')",
                "label": "Button label",
                "type": "button",
                "name": "test-button",
                "extra_classes": "",
            },
            {
                "onclick": "alert('test button action')",
                "label": "Button 2 label",
                "type": "button",
                "name": "test-button-2",
                "extra_classes": "fr-btn--secondary",
            },
        ],
    }

    context = Context({"test_data": test_data})
    template_to_render = Template(
        "{% load dsfr_tags %} {% dsfr_button_group test_data %}"
    )

    def test_button_group_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <ul class="fr-btns-group fr-btns-group--equisized">
                <li>
                    <button class="fr-btn"
                        onclick="alert(&#x27;test button action&#x27;)"
                        type="button"
                        name="test-button">
                    Button label
                    </button>
                </li>

                <li>
                    <button class="fr-btn fr-btn--secondary"
                        onclick="alert(&#x27;test button action&#x27;)"
                        type="button"
                        name="test-button-2">
                        Button 2 label
                    </button>
                </li>
            </ul>
            """,
            rendered_template,
        )


class DsfrCalloutTagTest(SimpleTestCase):
    test_data = {
        "text": "Text of the callout item",
        "title": "Title of the callout item",
        "icon_class": "fr-icon-information-line",
        "heading_tag": "h4",
        "button": {"onclick": "close()", "label": "button label", "type": "button"},
    }

    context = Context({"test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_callout test_data %}")

    def test_callout_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
    <p class="fr-callout__text">
        Text of the callout item
    </p>""",
            rendered_template,
        )

    def test_callout_optional_title_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """<h4 class="fr-callout__title">Title of the callout item</h4>""",
            rendered_template,
        )

    def test_callout_optional_icon_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertTrue("fr-icon-information-line" in rendered_template)

    def test_callout_optional_button_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <button
                type="button"
                class="fr-btn"
                onclick="close()"
            >
                button label
            </button>
            """,
            rendered_template,
        )


class DsfrCardTagTest(SimpleTestCase):
    card_data = {
        "top_detail": {"detail": {"text": "Appears before the title of the card item"}},
        "title": "Title of the card item",
        "description": "Text of the card item",
        "image_url": "https://test.gouv.fr/test.png",
        "link": "https://test.gouv.fr",
    }

    extra_classes = "test-extraclass"
    new_tab = True

    context = Context(
        {"card_data": card_data, "extra_classes": extra_classes, "new_tab": new_tab}
    )
    template_to_render = Template(
        "{% load dsfr_tags %} {% dsfr_card card_data extra_classes=extra_classes new_tab=newtab %}"  # noqa
    )

    def test_card_is_created(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertTrue("fr-card" in rendered_template)

    def test_card_has_detail(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            '<p class="fr-card__detail">Appears before the title of the card item</p>',
            rendered_template,
        )

    def test_card_has_title(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
                <p class="fr-card__title">
                <a href="https://test.gouv.fr" target="_self">
                    Title of the card item
                </a>
            </p>""",
            rendered_template,
        )

    def test_card_has_description(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            '<p class="fr-card__desc">Text of the card item</p>',
            rendered_template,
        )

    def test_card_has_optional_image(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <div class="fr-card__img">
                <img src="https://test.gouv.fr/test.png" class="fr-responsive-img" alt="">
            </div>
            """,  # noqa
            rendered_template,
        )


class DsfrConsentTagTest(SimpleTestCase):
    test_data = {
        "title": "À propos des cookies sur Django-DSFR",
        "content": """
                Bienvenue ! Nous utilisons des cookies pour améliorer votre expérience et les
                services disponibles sur ce site. Pour en savoir plus, visitez la page <a href="#">
                Données personnelles et cookies</a>. Vous pouvez, à tout moment, avoir le contrôle
                sur les cookies que vous souhaitez activer.
                """,
    }

    context = Context({"test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_consent test_data %}")

    def test_consent_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <div class="fr-consent-banner">
            <h2 class="fr-h6">
                À propos des cookies sur Django-DSFR
            </h2>
            <div class="fr-consent-banner__content">
                <p class="fr-text--sm">
                    Bienvenue ! Nous utilisons des cookies pour améliorer votre expérience et les
                    services disponibles sur ce site. Pour en savoir plus, visitez la page <a href="#">
                    Données personnelles et cookies</a>. Vous pouvez, à tout moment, avoir le contrôle
                    sur les cookies que vous souhaitez activer.
                </p>
            </div>
            <ul class="fr-consent-banner__buttons fr-btns-group fr-btns-group--right fr-btns-group--inline-reverse fr-btns-group--inline-sm">
                <li>
                <button class="fr-btn"
                        id="consent-accept-all"
                        title="Autoriser tous les cookies">
                    Tout accepter
                </button>
                </li>
                <li>
                <button class="fr-btn"
                        id="consent-reject-all"
                        title="Refuser tous les cookies">
                    Tout refuser
                </button>
                </li>
                <li>
                <button class="fr-btn fr-btn--secondary"
                        id="consent-customize"
                        data-fr-opened="false"
                        aria-controls="fr-consent-modal"
                        title="Personnaliser les cookies">
                    Personnaliser
                </button>
                </li>
            </ul>
            </div>
            """,
            rendered_template,
        )


class DsfrContentTagTest(SimpleTestCase):
    test_data = {
        "alt_text": "Silhouette stylisée représentant le soleil au-dessus de deux montagnes.",
        "caption": "Image en largeur normale et en 4x3",
        "image_url": "/django-dsfr/static/img/placeholder.16x9.svg",
        "ratio_class": "fr-ratio-4x3",
    }

    context = Context({"test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_content test_data %}")

    def test_content_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <figure class="fr-content-media" role="group" aria-label="Image en largeur normale et en 4x3">
            <div class="fr-content-media__img">
                <img class="fr-responsive-img fr-ratio-4x3"
                    src="/django-dsfr/static/img/placeholder.16x9.svg"
                    alt="Silhouette stylisée représentant le soleil au-dessus de deux montagnes." />
            </div>
                <figcaption class="fr-content-media__caption">
                Image en largeur normale et en 4x3
                </figcaption>
            </figure>""",
            rendered_template,
        )


class DsfrFranceConnectTagTest(SimpleTestCase):
    test_data = {"id": "france-connect"}

    context = Context({"test_data": test_data})
    template_to_render = Template(
        "{% load dsfr_tags %} {% dsfr_france_connect test_data %}"
    )

    def test_franceconnect_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <div class="fr-connect-group">
                <button class="fr-connect"
                        id="france-connect">
                    <span class="fr-connect__login">S’identifier avec</span>
                    <span class="fr-connect__brand">FranceConnect</span>
                </button>
                <p>
                    <a href="https://franceconnect.gouv.fr/"
                        target="_blank"
                        rel="noopener"
                        title="Qu’est-ce que FranceConnect ? - Ouvre une nouvelle fenêtre">Qu’est-ce que FranceConnect ?</a>
                </p>
            </div>
            """,
            rendered_template,
        )


class DsfrFranceConnectPlusTagTest(SimpleTestCase):
    test_data = {"id": "france-connect-plus", "plus": True}

    context = Context({"test_data": test_data})
    template_to_render = Template(
        "{% load dsfr_tags %} {% dsfr_france_connect test_data %}"
    )

    def test_franceconnectplus_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <div class="fr-connect-group">
                <button class="fr-connect fr-connect--plus"
                        id="france-connect-plus">
                    <span class="fr-connect__login">S’identifier avec</span>
                    <span class="fr-connect__brand">FranceConnect</span>
                </button>
                <p>
                    <a href="https://franceconnect.gouv.fr/france-connect-plus"
                        target="_blank"
                        rel="noopener"
                        title="Qu’est-ce que FranceConnect+ ? - Ouvre une nouvelle fenêtre">Qu’est-ce que FranceConnect+ ?</a>
                </p>
            </div>
            """,
            rendered_template,
        )


class DsfrHighlightTagTest(SimpleTestCase):
    test_data = {
        "content": "Content of the highlight item (can include html)",
        "title": "(Optional) Title of the highlight item",
        "heading_tag": "h4",
        "size_class": "fr-text--sm",
    }

    context = Context({"test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_highlight test_data %}")

    def test_highlight_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <div class="fr-highlight">
                <p class="fr-text--sm">
                    Content of the highlight item (can include html)
                </p>
            </div>
            """,
            rendered_template,
        )


class DsfrInputTagTest(SimpleTestCase):
    test_data_text = {
        "id": "sample-id",
        "label": "Label of the input item",
        "type": "text",
        "onchange": "doStuff()",
        "value": "Sample value",
    }

    test_data_date = {
        "id": "sample-id",
        "label": "Label of the input item",
        "type": "date",
        "onchange": "doStuff()",
        "value": "2021-09-15",
        "min": "2021-09-03",
        "max": "2021-04-21",
    }

    def test_text_input_tag_rendered(self):
        context = Context({"test_data": self.test_data_text})
        template_to_render = Template("{% load dsfr_tags %} {% dsfr_input test_data %}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """
            <div class="fr-input-group ">
                <label class="fr-label" for="sample-id">
                Label of the input item
                </label>
                <input
                    class="fr-input"
                    type="text"
                    id="sample-id"
                    name="sample-id"
                    onchange="doStuff()"
                    value="Sample value"
                />
            </div>
            """,
            rendered_template,
        )

    def test_date_input_tag_rendered(self):
        context = Context({"test_data": self.test_data_date})
        template_to_render = Template("{% load dsfr_tags %} {% dsfr_input test_data %}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """
            <div class="fr-input-group ">
                <label class="fr-label" for="sample-id">
                Label of the input item
                </label>
                <input
                    class="fr-input"
                    type="date"
                    id="sample-id"
                    name="sample-id"
                    onchange="doStuff()"
                    value="2021-09-15"
                    min="2021-09-03"
                    max="2021-04-21"
                />
            </div>
            """,
            rendered_template,
        )


class DsfrLinkTagTest(SimpleTestCase):
    test_data = {
        "url": "http://example.com",
        "label": "Label of the link item",
        "is_external": True,
        "extra_classes": "fr-link--lg",
    }

    context = Context({"test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_link test_data %}")

    def test_link_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <a
            class="fr-link fr-icon-external-link-line fr-link--icon-right fr-link--lg"
            href="http://example.com"
            target="_blank" rel="noopener noreferrer"
            >
              Label of the link item <span class="fr-sr-only">Ouvre une nouvelle fenêtre</span>
            </a>
            """,  # noqa
            rendered_template,
        )


class DsfrNoticeTagTest(SimpleTestCase):
    test_data = {
        "title": """Bandeau d’information importante avec <a href='#'
                            rel='noopener external'
                            title="intitulé - Ouvre une nouvelle fenêtre" target='_blank'>
                            lien</a>.""",
        "is_collapsible": True,
    }

    context = Context({"test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_notice test_data %}")

    def test_notice_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <div class="fr-notice__body">
                <p>
                    <span class="fr-notice__title">
                        Bandeau d’information importante avec <a href='#'
                            rel='noopener external'
                            title="intitulé - Ouvre une nouvelle fenêtre" target='_blank'>
                            lien</a>.
                    </span>
                </p>
                    <button class="fr-btn--close fr-btn"
                        title="Masquer le message"
                        onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)">
                    Masquer le message
                    </button>
                </div>
            """,  # noqa
            rendered_template,
        )


class DsfrQuoteTagTest(SimpleTestCase):
    test_data = {
        "text": "Développer vos sites et applications en utilisant des composants prêts à l'emploi, accessibles et ergonomiques",  # noqa
        "source_url": "https://www.systeme-de-design.gouv.fr/",
        "author": "Auteur",
        "source": "Système de Design de l'État",
        "details": [
            {"text": "Détail sans lien"},
            {
                "text": "Détail avec lien",
                "link": "https://template.incubateur.net/",
            },
        ],
        "image_url": "https://via.placeholder.com/150x150",
    }
    context = Context({"test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_quote test_data %}")

    def test_quote_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <figure class="fr-quote fr-quote--column">
                <blockquote cite="https://www.systeme-de-design.gouv.fr/">
                    <p>Développer vos sites et applications en utilisant des composants prêts à l&#x27;emploi, accessibles et ergonomiques</p>
                </blockquote>
                <figcaption>
                    <p class="fr-quote__author">Auteur</p>
                    <ul class="fr-quote__source">
                    <li>
                        <cite>Système de Design de l&#x27;État</cite>
                    </li>
                    <li>Détail sans lien</li>
                    <li><a target="_blank" rel="noopener noreferrer" href="https://template.incubateur.net/">Détail avec lien <span class="fr-sr-only">Ouvre une nouvelle fenêtre</span></a></li>
                    </ul>
                    <div class="fr-quote__image">
                    <img src="https://via.placeholder.com/150x150" class="fr-responsive-img" alt="" />
                    </div>
                </figcaption>
            </figure>
            """,  # noqa
            rendered_template,
        )


class DsfrSidemenuTagTest(SimpleTestCase):
    test_data = {
        "title": "Menu",
        "heading_tag": "h2",
        "id": "example",
        "items": [
            {
                "label": "Menu replié",
                "items": [
                    {
                        "label": "Une page",
                        "link": "#",
                    },
                    {
                        "label": "Une autre page",
                        "link": "/sidemenu",
                    },
                ],
            },
            {
                "label": "Menu ouvert",
                "items": [
                    {
                        "label": "Sous-menu replié",
                        "items": [
                            {"label": "Encore une page", "link": "#"},
                        ],
                    },
                    {
                        "label": "Sous-menu ouvert",
                        "items": [
                            {"label": "Page non active", "link": "#"},
                            {
                                "label": "Page active",
                                "link": "/django-dsfr/components/sidemenu/",
                            },
                        ],
                    },
                ],
            },
        ],
    }

    request_mock = MagicMock()
    request_mock.path = "/django-dsfr/components/sidemenu/"
    context = Context({"request": request_mock, "test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_sidemenu test_data %}")
    rendered_template = template_to_render.render(context)

    def test_sidemenu_tag_rendered(self):
        self.assertInHTML(
            """
            <li class="fr-sidemenu__item">
                <a class="fr-sidemenu__link" href="#" target="_self" >Une page</a>
            </li>

            """,
            self.rendered_template,
        )

    def test_sidemenu_heading_can_be_set(self):
        self.assertInHTML(
            """
            <h2 class="fr-sidemenu__title">Menu</h2>
            """,
            self.rendered_template,
        )

    def test_sidemenu_tag_current_page_and_parents_are_active(self):
        self.assertInHTML(
            """
            <li class="fr-sidemenu__item fr-sidemenu__item--active">
                <button
                    type="button"
                    class="fr-sidemenu__btn"
                    aria-expanded="true"
                    aria-controls="fr-sidemenu-example-item-2-2"
                >
                    Sous-menu ouvert
                </button>
                <div class="fr-collapse" id="fr-sidemenu-example-item-2-2">
                    <ul class="fr-sidemenu__list">
                        <li class="fr-sidemenu__item">
                        <a class="fr-sidemenu__link" href="#" target="_self" >
                            Page non active
                        </a>
                        </li>

                        <li class="fr-sidemenu__item fr-sidemenu__item--active">
                        <a class="fr-sidemenu__link" href="/django-dsfr/components/sidemenu/" target="_self"  aria-current="page">
                            Page active
                        </a>
                        </li>
                    </ul>
                </div>
            </li>
            """,  # noqa
            self.rendered_template,
        )


class DsfrSummaryTagTest(SimpleTestCase):
    test_data = [
        {"link": "link 1", "label": "First item title"},
        {"link": "link 2", "label": "Second item title"},
    ]

    context = Context({"test_data": test_data})
    template_to_render = Template(
        "{% load dsfr_tags %} {% dsfr_summary test_data summary_id='example' %}"
    )

    def test_summary_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <nav role="navigation" class="fr-summary" aria-labelledby="fr-summary-example-title">
                <p class="fr-summary__title" id="fr-summary-example-title">Sommaire</p>
                <ol class="fr-summary__list">

                    <li>
                        <a class="fr-summary__link" href="link 1">First item title</a>
                    </li>

                    <li>
                        <a class="fr-summary__link" href="link 2">Second item title</a>
                    </li>
                </ol>
            </nav>
            """,  # noqa
            rendered_template,
        )


class DsfrSkiplinksTagTest(SimpleTestCase):
    test_data = [
        {"link": "#contenu", "label": "Contenu"},
        {"link": "#header-navigation", "label": "Menu"},
    ]

    context = Context({"test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_skiplinks test_data %}")

    def test_summary_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <div class="fr-skiplinks">
                <nav role="navigation" class="fr-container" aria-label="Accès rapide">
                    <ul class="fr-skiplinks__list">
                    <li>
                        <a class="fr-link" href="#contenu">Contenu</a>
                    </li>
                    <li>
                        <a class="fr-link" href="#header-navigation">Menu</a>
                    </li>
                    </ul>
                </nav>
            </div>
            """,
            rendered_template,
        )


class DsfrTagTagTest(SimpleTestCase):
    def test_basic_tag_rendered(self):
        test_data = {
            "label": "Label of the tag item",
        }

        context = Context({"test_data": test_data})
        template_to_render = Template("{% load dsfr_tags %} {% dsfr_tag test_data %}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """<p class="fr-tag">Label of the tag item</p>""", rendered_template
        )

    def test_tag_with_link_rendered(self):
        test_data = {"label": "Label of the tag item", "link": "/components"}

        context = Context({"test_data": test_data})
        template_to_render = Template("{% load dsfr_tags %} {% dsfr_tag test_data %}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """<a href="/components" class="fr-tag">Label of the tag item</a>""",
            rendered_template,
        )

    def test_tag_with_icon_rendered(self):
        test_data = {"label": "Label of the tag item"}

        context = Context({"test_data": test_data})
        template_to_render = Template(
            "{% load dsfr_tags %} {% dsfr_tag test_data extra_classes='fr-icon-arrow-right-line fr-tag--icon-left' %}"  # noqa
        )
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """<p class="fr-tag fr-icon-arrow-right-line fr-tag--icon-left">Label of the tag item</p>""",  # noqa
            rendered_template,
        )

    def test_tag_with_action_rendered(self):
        test_data = {
            "label": "Label of the tag item",
            "link": "#",
            "onclick": "console.log('clicked');",
        }

        context = Context({"test_data": test_data})
        template_to_render = Template("{% load dsfr_tags %} {% dsfr_tag test_data %}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """<a href="#" class="fr-tag" onclick="console.log(&#x27;clicked&#x27;);">Label of the tag item</a>""",  # noqa
            rendered_template,
        )

    def test_tag_dismissable_rendered(self):
        test_data = {
            "label": "Label of the tag item",
            "is_dismissable": True,
        }

        context = Context({"test_data": test_data})
        template_to_render = Template("{% load dsfr_tags %} {% dsfr_tag test_data %}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """<button type="button" class="fr-tag fr-tag--dismiss" aria-label="Retirer le filtre Label of the tag item" onclick="event.preventDefault(); this.parentNode.removeChild(this);">Label of the tag item</button>""",  # noqa
            rendered_template,
        )


class DsfrToggleTagTest(SimpleTestCase):
    def test_toggle_rendered(self):
        test_data = {
            "label": "Interrupteur complet aligné à gauche",
            "help_text": "Cet interrupteur présente toutes les options disponibles",
            "is_disabled": False,
            "extra_classes": "fr-toggle--label-left fr-toggle--border-bottom",
            "id": "toggle-full",
        }

        context = Context({"test_data": test_data})
        template_to_render = Template(
            "{% load dsfr_tags %} {% dsfr_toggle test_data %}"
        )
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """
            <div class="fr-toggle fr-toggle--label-left fr-toggle--border-bottom">
                <input type="checkbox"
                        class="fr-toggle__input"
                        aria-describedby="toggle-full-hint-text"
                        id="toggle-full">
                <label class="fr-toggle__label"
                        for="toggle-full"
                        data-fr-checked-label="Activé"
                        data-fr-unchecked-label="Désactivé">
                    Interrupteur complet aligné à gauche
                </label>
                    <p class="fr-hint-text" id="toggle-full-hint-text">
                    Cet interrupteur présente toutes les options disponibles
                    </p>
                </div>
            """,
            rendered_template,
        )


class DsfrTooltipTagTest(SimpleTestCase):
    def test_tooltip_rendered(self):
        test_data = {
            "content": "Contenu d’une infobule activée au survol",
            "label": "Libellé du lien",
            "id": "tooltip-test",
        }

        context = Context({"test_data": test_data})
        template_to_render = Template(
            "{% load dsfr_tags %} {% dsfr_tooltip test_data %}"
        )
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """
            <a class="fr-link"
                aria-describedby="tooltip-test"
                id="link-tooltip-test"
                href="#">
                Libellé du lien
            </a>

            <span class="fr-tooltip fr-placement"
                id="tooltip-test"
                role="tooltip"
                aria-hidden="true">Contenu d’une infobule activée au survol</span>
            """,
            rendered_template,
        )


class DsfrTranscriptionTagTest(SimpleTestCase):
    test_data = {
        "content": "<div><p>Courte transcription basique</p></div>",
        "id": "transcription-test",
    }

    context = Context({"test_data": test_data})
    template_to_render = Template(
        "{% load dsfr_tags %} {% dsfr_transcription test_data %}"
    )

    def test_summary_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <div class="fr-transcription">
                <button class="fr-transcription__btn"
                        aria-expanded="false"
                        aria-controls="fr-transcription__collapse-transcription-test">
                    Transcription
                </button>
                <div class="fr-collapse" id="fr-transcription__collapse-transcription-test">
                    <div class="fr-transcription__footer">
                        <div class="fr-transcription__actions-group">

                            <button class="fr-btn fr-btn--fullscreen"
                                    aria-controls="fr-transcription-modal-transcription-test"
                                    data-fr-opened="false"
                                    title="Agrandir">
                                Agrandir
                            </button>
                        </div>
                    </div>
                    <dialog id="fr-transcription-modal-transcription-test"
                            class="fr-modal"
                            role="dialog"
                            aria-labelledby="fr-transcription-modal-transcription-test-title">
                        <div class="fr-container fr-container--fluid fr-container-md">
                            <div class="fr-grid-row fr-grid-row--center">
                                <div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
                                    <div class="fr-modal__body">
                                        <div class="fr-modal__header">

                                            <button class="fr-btn--close fr-btn"
                                                    aria-controls="fr-transcription-modal-transcription-test"
                                                    title="Fermer">
                                                Fermer
                                            </button>
                                        </div>
                                        <div class="fr-modal__content">
                                            <h1 id="fr-transcription-modal-transcription-test-title"
                                                class="fr-modal__title">
                                                Transcription
                                            </h1>
                                            <div><p>Courte transcription basique</p></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </dialog>
                </div>
            </div>
            """,  # noqa
            rendered_template,
        )


class ConcatenateTestCase(SimpleTestCase):
    def test_normal_concatenation(self):
        result = concatenate("test ", "value")
        self.assertEqual(result, "test value")

    def test_concatenation_with_empty_string(self):
        result = concatenate("test ", "")
        self.assertEqual(result, "test ")

    def test_concatenation_with_a_number(self):
        result = concatenate("test ", 3)
        self.assertEqual(result, "test 3")


class HyphenateTestCase(SimpleTestCase):
    def test_normal_hyphenation(self):
        result = hyphenate("test", "value")
        self.assertEqual(result, "test-value")

    def test_empty_value_is_not_hyphenated(self):
        result = hyphenate("test", "")
        self.assertEqual(result, "test")

    def test_numbers_can_be_hyphenated(self):
        result = hyphenate(4, 3)
        self.assertEqual(result, "4-3")

    def test_numbers_and_string_can_be_hyphenated(self):
        result = hyphenate("test", 3)
        self.assertEqual(result, "test-3")


class StrfmtTestCase(SimpleTestCase):
    def test_single_arg(self):
        self.assertEqual(
            "The sum of 1 + 2 is 3",
            Template(
                '{% load dsfr_tags %}{{ ctx_variable|strfmt:"The sum of 1 + 2 is {}" }}'
            ).render(Context({"ctx_variable": 1 + 2})),
        )

    def test_args(self):
        self.assertEqual(
            "The sum of 1 + 2 is 3 and it's awesome",
            Template(
                "{% load dsfr_tags %}"
                """{{ ctx_variable|strfmt:"The sum of 1 + 2 is {0} and it's {1}" }}"""
            ).render(Context({"ctx_variable": [1 + 2, "awesome"]})),
        )

    def test_single_kwargs(self):
        self.assertEqual(
            "The sum of 1 + 2 is 3 and it's awesome",
            Template(
                "{% load dsfr_tags %}"
                """{{ ctx_variable|strfmt:"The sum of 1 + 2 is {add_result} and it's {result_feeling}" }}"""
            ).render(
                Context(
                    {
                        "ctx_variable": {
                            "add_result": 1 + 2,
                            "result_feeling": "awesome",
                        }
                    }
                )
            ),
        )
