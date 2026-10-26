set dotenv-load
set shell := ["bash", "-uc"]

# Variables initialized from env
host_url := env("HOST_URL", "localhost")
local_port := env("LOCAL_PORT", "8000")

# List all recipes
default:
    @just --list

#### Django commands

# Pass a django command
[group('Django')]
django +command:
    uv run python manage.py {{command}}

# Compile translated messages
[group('Django')]
compilemessages:
    uv run django-admin compilemessages

# Collect static files
[group('Django')]
collectstatic:
    uv run python manage.py collectstatic --noinput

# Create a superuser
[group('Django')]
createsuperuser:
    uv run python manage.py createsuperuser

alias messages := makemessages
# Update localization files for translation
[group('Django')]
makemessages:
    uv run django-admin makemessages -l fr --ignore=manage.py,docs/*

alias rs := runserver
# Run the development server
[group('Django')]
runserver host_url=host_url local_port=local_port:
    uv run python manage.py runserver {{host_url}}:{{local_port}}

# Open a Django shell
[group('Django')]
shell:
    uv run python manage.py shell

#### Code audit

# Make quality checks on the whole project
[group('Code audit')]
quality:
    uv run prek run --all-files

# Run static type checks
[group('Code audit')]
typecheck:
    uv run pyright

#### Static export

# Export a static version of the site
[group('Static export')]
export_static:
    uv run python manage.py migrate
    uv run python manage.py import_sample_data
    uv run python manage.py distill-local docs --force --collectstatic
    uv run python manage.py export_json

# Run the site created through the export_static recipe
[group('Static export')]
static_server local_port=local_port:
    uv run python -m http.server 1{{local_port}} -d docs/

#### Tests

# Check test coverage
[group('Tests')]
coverage app="":
    uv run coverage run --source='.' manage.py test {{app}}
    uv run coverage html
    firefox htmlcov/index.html

# Run the unit tests
[group('Tests')]
test app="":
    uv run python manage.py test {{app}}

#### Utils

# Generate a secret key
[group('Utils')]
generate_secret_key:
    uv run python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

#### Setup

# Instantiate the project
[group('Setup')]
init:
    uv sync --dev --all-extras
    uv run prek install --overwrite
    uv run python manage.py migrate
    just collectstatic
    uv run python manage.py import_sample_data

#### Maintenance

# Update the DSFR version
[group('Maintenance')]
update_dsfr:
    bash scripts/download_latest.sh
    uv run python manage.py trim_dist
    uv run python manage.py integrity_checksums
    uv run python manage.py make_icon_picker_files
    just collectstatic

# Upgrade dependencies
[group('Maintenance')]
upgrade:
    uv lock --upgrade
    uv run prek update --cooldown-days 7

# Prepare a new release
[arg('bump', pattern='major|minor|patch')]
[group('Maintenance')]
prepare_release bump repo_name='origin':
    #!/usr/bin/env bash

    set -e

    version=`uv version --bump {{bump}} --short`
    echo "Version will be bumped to: $version"
    git switch -c "release/$version"
    uv version "$version"
    git add pyproject.toml uv.lock
    git commit -m "chore: prepare release $version"
    git push -u {{repo_name}} "release/$version"
