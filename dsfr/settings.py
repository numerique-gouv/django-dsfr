import warnings

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

if hasattr(settings, "DSFR_MARK_FORM_FIELDS"):
    if settings.DSFR_MARK_FORM_FIELDS not in ("required", "optional", None):
        raise ImproperlyConfigured(
            "Setting DSFR_MARK_FORM_FIELDS must be any of 'required', 'optional', None"
        )
    mark_form_fields = settings.DSFR_MARK_FORM_FIELDS
else:
    mark_form_fields = "required"

if mark_form_fields == "required":
    warnings.warn(
        "Marking required form fields is not recommended by DSFR so it will be removed soon. Please consider setting DSFR_MARK_FORM_FIELDS to either 'optional' (to mark optional fields) or None (to mark nothing).",
        DeprecationWarning,
        stacklevel=3,
    )
