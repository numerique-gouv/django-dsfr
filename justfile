set dotenv-load
set shell := ["bash", "-uc"]

# Variables initialized from env
host_url := env("HOST_URL", "localhost")
local_port := env("LOCAL_PORT", "8000")

# Default recipe
default:
    @just --list

# Other recipes
compilemessages:
    uv run django-admin compilemessages

collectstatic:
    uv run python manage.py collectstatic --noinput

coverage app="":
    uv run coverage run --source='.' manage.py test {{app}}
    uv run coverage html
    firefox htmlcov/index.html

createsuperuser:
    uv run python manage.py createsuperuser

export_static:
    uv run python manage.py migrate
    uv run python manage.py import_sample_data
    uv run python manage.py distill-local docs --force --collectstatic
    uv run python manage.py export_json

init:
    uv sync
    uv run pre-commit install
    uv run python manage.py migrate
    just collectstatic
    uv run python manage.py import_sample_data

alias messages := makemessages
makemessages:
    uv run django-admin makemessages -l fr --ignore=manage.py,docs/*

quality:
    uv run pre-commit run --all-files

alias rs := runserver
runserver host_url=host_url local_port=local_port:
    uv run python manage.py runserver {{host_url}}:{{local_port}}

shell:
    uv run python manage.py shell

static_server local_port=local_port:
    uv run python -m http.server 1{{local_port}} -d docs/

test app="":
    uv run python manage.py test {{app}}

update_dsfr:
    bash scripts/download_latest.sh
    uv run python manage.py trim_dist
    uv run python manage.py integrity_checksums
    uv run python manage.py make_icon_picker_files
    just collectstatic

upgrade:
    uv lock --upgrade
    uv run pre-commit autoupdate
