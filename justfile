set dotenv-load
set shell := ["bash", "-uc"]

# Variables initialized from env
host_url := env("HOST_URL", "localhost")
local_port := env("LOCAL_PORT", "8000")

# Default recipe
default:
    @just --list

# Other recipes

# Compile translated messages
compilemessages:
    uv run django-admin compilemessages

# Collect static files
collectstatic:
    uv run python manage.py collectstatic --noinput

# Check test coverage
coverage app="":
    uv run coverage run --source='.' manage.py test {{app}}
    uv run coverage html
    firefox htmlcov/index.html

# Create a superuser
createsuperuser:
    uv run python manage.py createsuperuser

# Export a static version of the site
export_static:
    uv run python manage.py migrate
    uv run python manage.py import_sample_data
    uv run python manage.py distill-local docs --force --collectstatic
    uv run python manage.py export_json

# Generate a secret key
generate_secret_key:
    uv_run python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Instantiate the project
init:
    uv sync
    uv run pre-commit install
    uv run python manage.py migrate
    just collectstatic
    uv run python manage.py import_sample_data

alias messages := makemessages
# Update localization files for translation
makemessages:
    uv run django-admin makemessages -l fr --ignore=manage.py,docs/*

# Make quality checks on the whole project
quality:
    uv run pre-commit run --all-files

alias rs := runserver
# Run the development server
runserver host_url=host_url local_port=local_port:
    uv run python manage.py runserver {{host_url}}:{{local_port}}

# Open a Django shell
shell:
    uv run python manage.py shell

# Run the site created through the export_static recipe
static_server local_port=local_port:
    uv run python -m http.server 1{{local_port}} -d docs/

# Run the unit tests
test app="":
    uv run python manage.py test {{app}}

# Update the DSFR version
update_dsfr:
    bash scripts/download_latest.sh
    uv run python manage.py trim_dist
    uv run python manage.py integrity_checksums
    uv run python manage.py make_icon_picker_files
    just collectstatic

# Upgrate dependencies
upgrade:
    uv lock --upgrade
    uv run pre-commit autoupdate

# Prepare a new release
[arg('bump', pattern='major|minor|patch')]
prepare_release bump:
    #!/usr/bin/env bash

    set -e

    version=`uv version --bump {{bump}} --short`
    echo "Version will be bumped to: $version"
    git switch -c "release/$version"
    uv version "$version"
    git add pyproject.toml uv.lock
    git commit -m "chore: prepare release $version"
    git push -u origin "release/$version"
