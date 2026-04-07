from django import template

register = template.Library()


@register.filter(is_safe=True)
def dsfr_md(content: str) -> str:
    from dsfr.markdown import markdown

    return markdown(content)


@register.filter(is_safe=True)
def dsfr_md_with_toc(content: str) -> str:
    from dsfr.markdown import markdown
    from dsfr.markdown import DsfrTocExtension

    return  markdown(content,extensions=[DsfrTocExtension()])

