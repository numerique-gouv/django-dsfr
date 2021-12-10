from django.conf import settings

from dsfr.models import DsfrConfig


def site_config(request):
    return {"SITE_CONFIG": DsfrConfig.objects.first()}
