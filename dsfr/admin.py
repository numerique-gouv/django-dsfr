from django.contrib import admin
from dsfr.models import DsfrConfig, DsfrSocialMedia

from django.utils.translation import gettext_lazy as _


class DsfrSocialMediaInline(admin.TabularInline):
    model = DsfrSocialMedia
    readonly_fields = ("id",)
    extra = 1


@admin.register(DsfrConfig)
class DsfrConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ("", {"fields": ("language",)}),
        (
            _("Website"),
            {
                "fields": (
                    ("site_title", "beta_tag"),
                    "site_tagline",
                    "mourning",
                )
            },
        ),
        (
            _("Notice"),
            {
                "fields": (
                    "notice_title",
                    "notice_description",
                    "notice_type",
                    "notice_link",
                    "notice_icon_class",
                    "notice_is_collapsible",
                ),
                "description": _(
                    "The important notice banner should only be used for essential and temporary information. \
                    (Excessive or continuous use risks “drowning” the message.)"
                ),
            },
        ),
        (
            _("Header"),
            {
                "fields": (
                    "header_brand",
                    "header_brand_html",
                ),
            },
        ),
        (
            _("Footer"),
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
            _("Operator logo"),
            {
                "fields": (
                    "operator_logo_file",
                    "operator_logo_alt",
                    "operator_logo_width",
                ),
            },
        ),
        (
            _("Newsletter"),
            {
                "fields": (
                    "newsletter_description",
                    "newsletter_url",
                )
            },
        ),
    )
    inlines = [DsfrSocialMediaInline]
