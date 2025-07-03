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
    poetry run django-admin compilemessages

collectstatic:
    poetry run python manage.py collectstatic --noinput

coverage app="":
    poetry run coverage run --source='.' manage.py test {{app}}
    poetry run coverage html
    firefox htmlcov/index.html

createsuperuser:
    poetry run python manage.py createsuperuser

export_static:
    poetry run python manage.py migrate
    poetry run python manage.py import_sample_data
    poetry run python manage.py distill-local docs --force --collectstatic
    poetry run python manage.py export_json

init:
    poetry install
    poetry run pre-commit install
    poetry run python manage.py migrate
    juyt collectstatic
    poetry run python manage.py import_sample_data

alias messages := makemessages
makemessages:
    poetry run django-admin makemessages -l fr --ignore=manage.py,docs/*

quality:
    poetry run pre-commit run --all-files

alias rs := runserver
runserver host_url=host_url local_port=local_port:
    poetry run python manage.py runserver {{host_url}}:{{local_port}}

static_server local_port=local_port:
    poetry run python -m http.server 1{{local_port}} -d docs/

test app="":
    poetry run python manage.py test {{app}}

update_dsfr:
    bash scripts/download_latest.sh
    poetry run python manage.py trim_dist
    poetry run python manage.py integrity_checksums
    poetry run python manage.py make_icon_picker_files
    just collectstatic

upgrade:
    poetry update
    poetry run pre-commit autoupdate
