"""
Deprecated: the integrity checksums are now computed on the fly.

Use `dsfr.utils.get_integrity()` or the `{% dsfr_integrity %}` template tag instead.
The values below are kept for backward compatibility.
"""

import warnings

from dsfr.constants import DsfrStaticAssets

_PATHS = {
    "INTEGRITY_JS_MODULE": DsfrStaticAssets.DSFR_MODULE_JS,
    "INTEGRITY_JS_NOMODULE": DsfrStaticAssets.DSFR_NOMODULE_JS,
    "INTEGRITY_CSS": DsfrStaticAssets.DSFR_CSS,
    "INTEGRITY_UTILITY_CSS": DsfrStaticAssets.DSFR_UTILITY_CSS,
}


def __getattr__(name: str) -> str:
    # Values are computed lazily, as settings and apps aren't ready at import time
    if name not in _PATHS:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    warnings.warn(
        "dsfr.checksums is deprecated, use dsfr.utils.get_integrity() "
        "or the {% dsfr_integrity %} template tag instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    from dsfr.utils import get_integrity

    return get_integrity(_PATHS[name]) or ""
