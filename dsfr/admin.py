from django.contrib import admin
from dsfr.models import DsfrConfig


@admin.register(DsfrConfig)
class DsfrConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Site", {"fields": ("site_title", "site_tagline")}),
        (
            "En-tête",
            {
                "fields": ("header_brand", "header_brand_html"),
            },
        ),
        (
            "Pied de page",
            {
                "fields": ("footer_brand", "footer_brand_html", "footer_description"),
            },
        ),
        (
            "Avancé",
            {
                "fields": ("mourning", "accessibility_status"),
            },
        ),
    )
