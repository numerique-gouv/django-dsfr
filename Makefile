# Loading environment variables
ifneq (,$(wildcard ./.env))
    include .env
    export LOCAL_PORT
endif

# Setting defaults for env variables
ifdef LOCAL_PORT
	local_port := $(LOCAL_PORT)
else
	local_port := 8000
endif

# Commands

.PHONY: collectstatic
collectstatic:
	poetry run python manage.py collectstatic --noinput

.PHONY: init
init:
	poetry install
	poetry run pre-commit install
	poetry run python manage.py migrate
	make collectstatic
	poetry run python manage.py import_sample_data
	poetry shell

.PHONY: messages
messages:
	poetry run django-admin makemessages -l fr --ignore=manage.py,docs/*

.PHONY: compilemessages
compilemessages:
	poetry run django-admin compilemessages

.PHONY: quality
quality:
	poetry run pre-commit run --all-files

.PHONY: runserver
runserver:
	poetry run python manage.py runserver $(local_port)

.PHONY: test
test:
	poetry run python manage.py test

.PHONY: update_dsfr
update_dsfr:
	bash scripts/download_latest.sh
	poetry run python manage.py trim_dist
	poetry run python manage.py integrity_checksums
	poetry run python manage.py make_icon_picker_files
	make collectstatic

.PHONY: static_server
static_server:
	python -m http.server 1$(local_port) -d docs/

.PHONY: export_static
export_static:
	poetry run python manage.py migrate
	poetry run python manage.py import_sample_data
	poetry run python manage.py distill-local docs --force --collectstatic
	poetry run python manage.py export_json
