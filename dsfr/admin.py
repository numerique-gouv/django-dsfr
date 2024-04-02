from django.contrib import admin
from dsfr.models import DsfrConfig


@admin.register(DsfrConfig)
class DsfrConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Site", {"fields": ("site_title", "site_tagline", "notice", "mourning")}),
        (
            "En-tête",
            {
                "fields": ("header_brand", "header_brand_html", "beta_tag"),
            },
        ),
        (
            "Pied de page",
            {
                "fields": (
                    "footer_brand",
                    "footer_brand_html",
                    "footer_description",
                    "accessibility_status",
                ),
            },
        ),
        (
            "Logo opérateur",
            {
                "fields": (
                    "operator_logo_file",
                    "operator_logo_alt",
                    "operator_logo_width",
                ),
            },
        ),
    )
