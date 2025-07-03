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

# Warnings
MAKEFLAGS += --no-print-directory
NO_FORMAT=\033[0m
C_ORANGERED1=\033[38;5;202m

.PHONY: deprecation-warning
deprecation-warning:
	@echo "${C_ORANGERED1}WARNING: this project now uses just instead of make. \
	This recipe is obsolete and will be removed in a future major version. \
	Please use the equivalent recipe through just.${NO_FORMAT}"

.PHONY: deletion-warning
deletion-warning:
	@echo "${C_ORANGERED1}WARNING: this recipe is obsolete \
	and will be removed in a future major version.${NO_FORMAT}"

# Commands

.PHONY: collectstatic
collectstatic:
	poetry run python manage.py collectstatic --noinput
	@make deprecation-warning

.PHONY: init
init:
	poetry install
	poetry run pre-commit install
	poetry run python manage.py migrate
	make collectstatic
	poetry run python manage.py import_sample_data
	@make deprecation-warning

.PHONY: messages
messages:
	poetry run django-admin makemessages -l fr --ignore=manage.py,docs/*
	@make deprecation-warning

.PHONY: compilemessages
compilemessages:
	poetry run django-admin compilemessages
	@make deprecation-warning

.PHONY: quality
quality:
	poetry run pre-commit run --all-files
	@make deprecation-warning

.PHONY: runserver
runserver:
	poetry run python manage.py runserver $(local_port)
	@make deprecation-warning

.PHONY: test
test:
	poetry run python manage.py test
	@make deprecation-warning

.PHONY: update_dsfr
update_dsfr:
	bash scripts/download_latest.sh
	poetry run python manage.py trim_dist
	poetry run python manage.py integrity_checksums
	poetry run python manage.py make_icon_picker_files
	make collectstatic
	@make deprecation-warning

.PHONY: upgrade
upgrade:
	poetry update
	poetry run pre-commit autoupdate
	@make deprecation-warning

.PHONY: static_server
static_server:
	python -m http.server 1$(local_port) -d docs/
	@make deprecation-warning

.PHONY: export_static
export_static:
	poetry run python manage.py migrate
	poetry run python manage.py import_sample_data
	poetry run python manage.py distill-local docs --force --collectstatic
	poetry run python manage.py export_json
	@make deprecation-warning
