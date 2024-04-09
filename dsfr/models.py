import os


from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from dsfr.constants import DJANGO_DSFR_LANGUAGES


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [".jpg", ".jpeg", ".png", ".svg"]
    if ext.lower() not in valid_extensions:
        raise ValidationError("Unsupported file extension.")


class DsfrConfig(models.Model):
    language = models.CharField(
        _("Language"),
        max_length=7,
        choices=DJANGO_DSFR_LANGUAGES,
        help_text=_("Only one configuration is allowed per language"),
        default="fr",
        unique=True,
    )

    A11Y_CHOICES = [
        ("FULL", _("fully")),
        ("PART", _("partially")),
        ("NOT", _("not")),
    ]

    # Site
    site_title = models.CharField(
        _("Site title"), max_length=200, default=_("Site title"), blank=True
    )
    site_tagline = models.CharField(
        _("Site tagline"), max_length=200, default=_("Site tagline"), blank=True
    )
    notice = models.TextField(
        _("Important notice"),
        default="",
        blank=True,
        help_text=_(
            "The important notice banner should only be used for essential and temporary information. \
            (Excessive or continuous use risks “drowning” the message.)"
        ),
    )

    # Header
    header_brand = models.CharField(
        _("Institution (header)"),
        max_length=200,
        default="République française",
        blank=True,
    )
    header_brand_html = models.CharField(
        _("Institution with line break (header)"),
        max_length=200,
        default="République<br />française",
        blank=True,
    )
    beta_tag = models.BooleanField(_("Show the BETA tag next to the title"), default=False)  # type: ignore

    # Footer
    footer_brand = models.CharField(
        _("Institution (footer)"),
        max_length=200,
        default="République française",
        blank=True,
    )
    footer_brand_html = models.CharField(
        _("Institution with line break (footer)"),
        max_length=200,
        default="République<br />française",
        blank=True,
    )
    footer_description = models.TextField(_("Description"), default="", blank=True)

    newsletter_description = models.TextField(
        _("Newsletter description"), default="", blank=True
    )

    newsletter_url = models.URLField(
        _("Newsletter registration URL"),
        default="",
        blank=True,
    )

    # Operator logo
    operator_logo_file = models.FileField(
        _("Operator logo"),
        upload_to="logos",
        blank=True,
        null=True,
        validators=[validate_image_extension],
    )
    operator_logo_alt = models.CharField(
        _("Logo alt text"),
        max_length=200,
        blank=True,
        help_text=_("Must contain the text present in the image."),
    )
    operator_logo_width = models.DecimalField(
        _("Width (em)"),
        max_digits=3,
        decimal_places=1,
        null=True,
        default="0.0",
        help_text=_(
            "To be adjusted according to the width of the logo.\
            Example for a vertical logo: 3.5, Example for a horizontal logo: 8."
        ),
    )

    # Advanced
    mourning = models.BooleanField(_("Mourning"), default=False)  # type: ignore

    accessibility_status = models.CharField(
        _("Accessibility compliance status"),
        max_length=4,
        choices=A11Y_CHOICES,
        default="NOT",
    )

    class Meta:
        verbose_name = _("Configuration")

    def __str__(self):
        return _("Site config:") + f" {self.site_title} ({self.language})"

    def social_media(self):
        return self.dsfrsocialmedia_set.all()


class DsfrSocialMedia(models.Model):
    site_config = models.ForeignKey(DsfrConfig, on_delete=models.CASCADE, null=True)
    title = models.CharField(_("Title"), max_length=200, default="", blank=True)

    url = models.URLField(
        _("URL"),
        default="",
        blank=True,
    )
    icon_class = models.CharField(
        _("Icon class"), max_length=200, default="", blank=True
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = _("Social media")
        verbose_name_plural = _("Social medias")
