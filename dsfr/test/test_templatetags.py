from dsfr.templatetags.dsfr_tags import concatenate, hyphenate
from django.test import SimpleTestCase
from django.template import Context, Template
from unittest.mock import MagicMock


class DsfrCssTagTest(SimpleTestCase):
    def test_css_tag_rendered(self):
        context = Context()
        template_to_render = Template("{% load dsfr_tags %} {% dsfr_css %}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            '<link rel="stylesheet" href="/django-dsfr/static/dsfr/dist/css/dsfr.min.css">',
            rendered_template,
        )


class DsfrJsTagTest(SimpleTestCase):
    def test_js_tag_rendered(self):
        context = Context()
        template_to_render = Template("{% load dsfr_tags %} {% dsfr_js %}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """
            <script type="module" src="/django-dsfr/static/dsfr/dist/js/dsfr.module.min.js"></script>
            <script type="text/javascript" nomodule src="/django-dsfr/static/dsfr/dist/js/dsfr.nomodule.min.js"></script>
            """,
            rendered_template,
        )


class DsfrFaviconTagTest(SimpleTestCase):
    def test_favicon_tag_rendered(self):
        context = Context()
        template_to_render = Template("{% load dsfr_tags %} {% dsfr_favicon %}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """
            <link rel="apple-touch-icon" href="/django-dsfr/static/dsfr/dist/favicons/apple-touch-icon.png"><!-- 180×180 -->
            <link rel="icon" href="/django-dsfr/static/dsfr/dist/favicons/favicon.svg" type="image/svg+xml">
            <link rel="shortcut icon" href="/django-dsfr/static/dsfr/dist/favicons/favicon.ico" type="image/x-icon">
            <!-- 32×32 -->
            <link rel="manifest" href="/django-dsfr/static/dsfr/dist/favicons/manifest.webmanifest"
            crossorigin="use-credentials">
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
            """,
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
            <button type="button" class="fr-link--close fr-link" aria-expanded="true" aria-controls="test-alert-message">
                Masquer le message
            </button>
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
        "extra_classes": "fr-btn--secondary",
    }

    context = Context({"test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_button test_data %}")

    def test_button_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <button
                type="button"
                class="fr-btn fr-btn--secondary"
                onclick="alert(&#x27;test button action&#x27;)"            
            >
                button label    
            </button>
            """,
            rendered_template,
        )


class DsfrCalloutTagTest(SimpleTestCase):
    test_data = {
        "text": "Text of the callout item",
        "title": "Title of the callout item",
        "icon_class": "fr-fi-information-line",
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
        self.assertTrue("fr-fi-information-line" in rendered_template)

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
        "detail": "Appears before the title of the card item",
        "title": "Title of the card item",
        "description": "Text of the card item",
        "image_url": "https://test.gouv.fr/test.png",
    }

    extra_classes = "test-extraclass"
    new_tab = True

    context = Context(
        {"card_data": card_data, "extra_classes": extra_classes, "new_tab": new_tab}
    )
    template_to_render = Template(
        "{% load dsfr_tags %} {% dsfr_card card_data extra_classes=extra_classes new_tab=newtab %}"
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
                <a href="" class="fr-card__link" target="_self">
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
            class="fr-link fr-fi-external-link-line fr-link--icon-right fr-link--lg"
            href="http://example.com"
            target="_blank" rel="noopener noreferrer"
            >
            Label of the link item
            </a>
            """,
            rendered_template,
        )


class DsfrQuoteTagTest(SimpleTestCase):
    test_data = {
        "text": "Développer vos sites et applications en utilisant des composants prêts à l'emploi, accessibles et ergonomiques",
        "source_url": "https://www.systeme-de-design.gouv.fr/",
        "author": "Auteur",
        "source": "Système de Design de l'État",
        "details": [
            {"text": "Detail sans lien"},
            {
                "text": "Detail avec lien",
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
                    <li>Detail sans lien</li>
                    <li><a target="_blank" rel="noopener noreferrer" href="https://template.incubateur.net/">Detail avec lien</a></li>
                    </ul>
                    <div class="fr-quote__image">
                    <img src="https://via.placeholder.com/150x150" class="fr-responsive-img" alt="" />
                    </div>
                </figcaption>
            </figure>
            """,
            rendered_template,
        )


class DsfrSidemenuTagTest(SimpleTestCase):
    test_data = {
        "title": "Menu",
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
                                "link": "/sidemenu/",
                            },
                        ],
                    },
                ],
            },
        ],
    }

    request_mock = MagicMock()
    request_mock.path = "/sidemenu/"
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

    def test_sidemenu_tag_current_page_and_parents_are_active(self):
        self.assertInHTML(
            """
            <li class="fr-sidemenu__item fr-sidemenu__item--active">
                <button
                    type="button"
                    class="fr-sidemenu__btn"
                    aria-expanded="true"
                    aria-controls="fr-sidemenu-item-2-2"
                >
                    Sous-menu ouvert
                </button>
                <div class="fr-collapse" id="fr-sidemenu-item-2-2">
                    <ul class="fr-sidemenu__list">
                    
                        <li class="fr-sidemenu__item">
                        <a class="fr-sidemenu__link" href="#" target="_self" >
                            Page non active
                        </a>
                        </li>
                    
                        <li class="fr-sidemenu__item fr-sidemenu__item--active">
                        <a class="fr-sidemenu__link" href="/sidemenu/" target="_self"  aria-current="page">
                            Page active
                        </a>
                        </li>
                    
                    </ul>
                </div>
            </li>
            """,
            self.rendered_template,
        )


class DsfrSummaryTagTest(SimpleTestCase):
    test_data = [
        {"link": "link 1", "label": "First item title"},
        {"link": "link 2", "label": "Second item title"},
    ]

    context = Context({"test_data": test_data})
    template_to_render = Template("{% load dsfr_tags %} {% dsfr_summary test_data %}")

    def test_summary_tag_rendered(self):
        rendered_template = self.template_to_render.render(self.context)
        self.assertInHTML(
            """
            <nav class="fr-summary" role="navigation" aria-labelledby="fr-summary-title">
                <div class="fr-summary__title" id="fr-summary-title">Sommaire</div>
                <ol class="fr-summary__list">
                    
                    <li>
                        <a class="fr-summary__link" href="link 1">First item title</a>
                    </li>
                    
                    <li>
                        <a class="fr-summary__link" href="link 2">Second item title</a>
                    </li>  
                </ol>
            </nav>
            """,
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
                <nav class="fr-container" role="navigation" aria-label="Accès rapide">
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
        test_data = {"label": "Label of the tag item", "link": "/tags"}

        context = Context({"test_data": test_data})
        template_to_render = Template("{% load dsfr_tags %} {% dsfr_tag test_data %}")
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """<a href="/tags" class="fr-tag">Label of the tag item</a>""",
            rendered_template,
        )

    def test_tag_with_icon_rendered(self):
        test_data = {"label": "Label of the tag item"}

        context = Context({"test_data": test_data})
        template_to_render = Template(
            "{% load dsfr_tags %} {% dsfr_tag test_data extra_classes='fr-fi-arrow-right-line fr-tag--icon-left' %}"
        )
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            """<p class="fr-tag fr-fi-arrow-right-line fr-tag--icon-left">Label of the tag item</p>""",
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
