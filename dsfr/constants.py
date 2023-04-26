# Integrity checks for the css/js/favicon files
# Generated with the following command:
# openssl dgst -sha384 -binary path/to/file.min.css | openssl base64 -A

#### JS
# dsfr/dist/dsfr/dsfr.module.min.js
INTEGRITY_JS_MODULE = (
    "sha384-I2h3dQPRm8wpUZxuuDoCO5k+q6jvFHVAcTkMeJJq/noEkqKDlj6TfbB/TRUgp0zO"
)
# dsfr/dist/dsfr/dsfr.nomodule.min.js
INTEGRITY_JS_NOMODULE = (
    "sha384-d+DDNW3pgRaE0MzYgb+MqZxgN/70LO9MiYA6q2Fc7ydJlu3jKx6MmI5EddVeYzl6"
)

#### CSS
# dsfr/dist/dsfr/dsfr.min.css
INTEGRITY_CSS = (
    "sha384-LtcfS1K2I3jMUhzjxpeUO3UUiin8SpxX5rODWf05CrGtS44FrX8oAYCPVaFbM10M"
)
# dsfr/dist/utility/icons/icons.min.css
INTEGRITY_CSS_ICONS = (
    "sha384-STqXIfO4sjaf/YUpwUezCvsCRtEmzt2vrpk5cixx+BPM6SWpOC6K8Bu5b9Svd3sV"
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
