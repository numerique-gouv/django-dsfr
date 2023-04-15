# Integrity checks for the css/js/favicon files
# Generated with the following command:
# openssl dgst -sha384 -binary path/to/file.min.css | openssl base64 -A

#### JS
# dsfr/dist/dsfr/dsfr.module.min.js
INTEGRITY_JS_MODULE = (
    "sha384-hsT8G3ewRLMSn+hcsZeqdjIsqjqMh/pD8TTc8egEcN4MpeNQDZ+7EqVXDW0zVfYm"
)
# dsfr/dist/dsfr/dsfr.nomodule.min.js
INTEGRITY_JS_NOMODULE = (
    "sha384-z+nnc/m3glran4qVg9/2tnMN5v0yvtoXgW4djyCn8npkBhm8uQ90QGYeQ7oqf7Bt"
)

#### CSS
# dsfr/dist/dsfr/dsfr.min.css
INTEGRITY_CSS = (
    "sha384-7z0V109kCjLc5JiwfCaR+gM7rwAw8pWsrgISPTlaD3B77TwopmDN3DQ20n36NMB2"
)
# dsfr/dist/utility/icons/icons.min.css
INTEGRITY_CSS_ICONS = (
    "sha384-J7lCkOU9dOy1LLABqcy542lznn5TyxJnWuFXMse5v7POyQlh95Esaw7RtKwNAHIP"
)

#### Favicon
# dsfr/dist/favicon/apple-touch-icon.png
INTEGRITY_FAVICON_APPLE = (
    "sha384-bE/sjT09LYXMMjd/7ovUY40XBU2WQoLkIRw4/eBcHdBVsJOhoomJuSSa+qEFGku/"
)
# dsfr/dist/favicon/favicon.svg
INTEGRITY_FAVICON_SVG = (
    "sha384-z4gMU2V+U4skVvrlEwyCe+lUVDhliQY6Tg0az69xNkmyu4H84cy+uJZnWVkHfMrN"
)
# dsfr/dist/favicon/favicon.ico
INTEGRITY_FAVICON_ICO = (
    "sha384-esZ1Wf54Wvb66vtrLBKzz2QEZciEIV9R+wc+w7C3e5mID8A1SgJpXXIc+3lY9YqP"
)
# dsfr/dist/favicon/manifest.webmanifest
INTEGRITY_FAVICON_MANIFEST = (
    "sha384-9rQ8jBh6MztX7GlSBVwj2yJEUaxKTCy3pYRLq1Qu57zkdJ3P5ftf6GyfYJwFuR7j"
)
