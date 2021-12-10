from django.db import models
from django.core.exceptions import ValidationError


class DsfrConfig(models.Model):
    A11Y_CHOICES = [
        ("FULL", "totalement"),
        ("PART", "partiellement"),
        ("NOT", "non"),
    ]

    header_brand = models.CharField(
        "Institution (en-tête)",
        max_length=200,
        default="République française",
        blank=True,
    )
    header_brand_html = models.CharField(
        "Institution avec césure (en-tête)",
        max_length=200,
        default="République<br />française",
        blank=True,
    )
    footer_brand = models.CharField(
        "Institution (pied)", max_length=200, default="République française", blank=True
    )
    footer_brand_html = models.CharField(
        "Institution avec césure (pied)",
        max_length=200,
        default="République<br />française",
        blank=True,
    )
    site_title = models.CharField(
        "Titre du site", max_length=200, default="Titre du site", blank=True
    )
    site_tagline = models.CharField(
        "Sous-titre du site", max_length=200, default="Sous-titre du site", blank=True
    )
    footer_description = models.TextField("Description", default="", blank=True)
    mourning = models.BooleanField("Mise en berne", default=False)
    accessibility_status = models.CharField(
        "Statut de conformité de l’accessibilité",
        max_length=4,
        choices=A11Y_CHOICES,
        default="NOT",
    )

    class Meta:
        verbose_name = "Configuration"

    def __str__(self):
        return f"Configuration du site : {self.site_title}"

    def save(self, *args, **kwargs):
        if not self.pk and DsfrConfig.objects.exists():
            raise ValidationError("There can be only one DsfrBaseSettings instance")
        return super(DsfrConfig, self).save(*args, **kwargs)
