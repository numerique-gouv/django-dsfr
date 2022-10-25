# Integrity checks for the css/js files
# Generated with the following command:
# openssl dgst -sha384 -binary path/to/file.min.css | openssl base64 -A


INTEGRITY_JS_MODULE = (
    "sha384-S0rArPSbImK+pbCuenUI94sCELE0j2TcUqSauDNeTLZxL3HBr6ilBWCzU6605Lhc"
)
INTEGRITY_JS_NOMODULE = (
    "sha384-/Ki29nOlnayQ7/etxVpEaxmfMye/syzFZVrgkd93WGAi4/WlVvVLhLp9GMvtPP+y"
)
INTEGRITY_CSS = (
    "sha384-C/tHGtxXFiwg9vEKg7jcH+8kQhlkUfq22JBeptJ8AqGHcArh9k/LdedUi42QQRRi"
)
INTEGRITY_CSS_ICONS = (
    "sha384-/chTXCOZpCTu7roNmemf+/rzzYwswg3UdqDqTYmx1sxYnJjDjvUWSfu+6lk02dHh"
)
