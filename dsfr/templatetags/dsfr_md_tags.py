import re

from django import template
from django.utils.safestring import mark_safe
from markdown import markdown
from markdown.blockprocessors import BlockProcessor, BlockQuoteProcessor
from markdown.inlinepatterns import LinkInlineProcessor, LINK_RE
from markdown.extensions.admonition import AdmonitionProcessor
from markdown.extensions.attr_list import AttrListExtension
from markdown.extensions.nl2br import Nl2BrExtension
from markdown.extensions.tables import TableProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree


register = template.Library()


class DsfrTableProcessorMixin(BlockProcessor):
    dsfr_bordered = False

    def run(self, parent, *args):
        super().run(parent, *args)

        # Build the DSFR-specific layers surrounding the <table>
        # cf https://www.systeme-de-design.gouv.fr/version-courante/fr/composants/tableau
        div = etree.SubElement(parent, "div")
        div.attrib["class"] = "fr-table"
        if self.dsfr_bordered:
            div.attrib["class"] += " fr-table--bordered"
        wrapper = etree.SubElement(div, "div")
        wrapper.attrib["class"] = "fr-table__wrapper"
        container = etree.SubElement(wrapper, "div")
        container.attrib["class"] = "fr-table__container"
        content = etree.SubElement(container, "div")
        content.attrib["class"] = "fr-table__content"

        # move the table from the parent to the lowest DSFR layer
        added_table = parent.find("table[last()]")
        parent.remove(added_table)
        content.append(added_table)


class DsfrTableProcessor(DsfrTableProcessorMixin, TableProcessor):
    pass


class DsfrCalloutProcessor(AdmonitionProcessor):
    CLASSNAME = "fr-callout"
    CLASSNAME_TITLE = "fr-callout__title"

    def run(self, parent: etree.Element, *args) -> None:
        super().run(parent, *args)
        div = parent.find("div")
        if any(
            (
                dsfr_icon_suffix in div.attrib["class"]
                for dsfr_icon_suffix in ("-line", "-fill")
            )
        ):
            div.attrib["class"] = div.attrib["class"].replace(" ", " fr-icon-")
        for child in div.findall("*"):
            if "class" in child.attrib:
                continue
            child.attrib["class"] = "fr-callout__text"


class DsfrHighlightProcessor(AdmonitionProcessor):
    CLASSNAME = "fr-highlight"
    RE = re.compile(r'(?:^|\n)!! ?([\w\-]+(?: +[\w\-]+)*)(?: +"(.*?)")? *(?:\n|$)')

    def get_class_and_title(self, match):
        return match.group(1).lower(), None


class DsfrQuoteProcessor(BlockQuoteProcessor):
    def run(self, parent: etree.Element, *args):
        super().run(parent, *args)
        figure = etree.SubElement(parent, "figure", {"class": "fr-quote"})
        blockquote = parent.find("blockquote")
        parent.remove(blockquote)
        figure.append(blockquote)


class DsfrLinkProcessor(LinkInlineProcessor):
    def handleMatch(self, *args):
        el, pos, idx = super().handleMatch(*args)
        if (
            hasattr(el, "attrib")
            and "href" in el.attrib
            and (
                el.attrib["href"].startswith("http://")
                or el.attrib["href"].startswith("https://")
            )
        ):
            el.attrib["target"] = "_blank"
            el.attrib["rel"] = "noopener external"
            el.attrib["title"] = f"{el.text.strip()} - nouvelle fenêtre"
        return el, pos, idx


class DsfrExtension(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(DsfrLinkProcessor(LINK_RE, md), "link", 200)
        md.parser.blockprocessors.register(
            DsfrTableProcessor(md.parser, self.getConfigs()), "table", 100
        )
        md.parser.blockprocessors.register(
            DsfrCalloutProcessor(md.parser), "dsfr-callout", 100
        )
        md.parser.blockprocessors.register(
            DsfrHighlightProcessor(md.parser), "dsfr-highlight", 100
        )
        md.parser.blockprocessors.register(
            DsfrQuoteProcessor(md.parser), "dsfr-quote", 100
        )


@register.filter(is_safe=True)
def dsfr_md(content: str) -> str:
    return mark_safe(
        markdown(
            content,
            extensions=[
                AttrListExtension(),
                DsfrExtension(),
                Nl2BrExtension(),
                "pymdownx.striphtml",
            ],
        )
    )
