# Integrity checks for the css/js/favicon files
# Generated with the following command:
# openssl dgst -sha384 -binary path/to/file.min.css | openssl base64 -A

# JS
INTEGRITY_JS_MODULE = (
    "sha384-S0rArPSbImK+pbCuenUI94sCELE0j2TcUqSauDNeTLZxL3HBr6ilBWCzU6605Lhc"
)
INTEGRITY_JS_NOMODULE = (
    "sha384-/Ki29nOlnayQ7/etxVpEaxmfMye/syzFZVrgkd93WGAi4/WlVvVLhLp9GMvtPP+y"
)

# CSS
INTEGRITY_CSS = (
    "sha384-C/tHGtxXFiwg9vEKg7jcH+8kQhlkUfq22JBeptJ8AqGHcArh9k/LdedUi42QQRRi"
)
INTEGRITY_CSS_ICONS = (
    "sha384-/chTXCOZpCTu7roNmemf+/rzzYwswg3UdqDqTYmx1sxYnJjDjvUWSfu+6lk02dHh"
)

# Favicon
INTEGRITY_FAVICON_APPLE = (
    "sha384-bE/sjT09LYXMMjd/7ovUY40XBU2WQoLkIRw4/eBcHdBVsJOhoomJuSSa+qEFGku/"
)
INTEGRITY_FAVICON_SVG = (
    "sha384-z4gMU2V+U4skVvrlEwyCe+lUVDhliQY6Tg0az69xNkmyu4H84cy+uJZnWVkHfMrN"
)
INTEGRITY_FAVICON_ICO = (
    "sha384-esZ1Wf54Wvb66vtrLBKzz2QEZciEIV9R+wc+w7C3e5mID8A1SgJpXXIc+3lY9YqP"
)
INTEGRITY_FAVICON_MANIFEST = (
    "sha384-9rQ8jBh6MztX7GlSBVwj2yJEUaxKTCy3pYRLq1Qu57zkdJ3P5ftf6GyfYJwFuR7j"
)
