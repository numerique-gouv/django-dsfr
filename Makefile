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
	uv run python manage.py collectstatic --noinput
	@make deprecation-warning

.PHONY: init
init:
	uv sync
	uv run pre-commit install
	uv run python manage.py migrate
	make collectstatic
	uv run python manage.py import_sample_data
	@make deprecation-warning

.PHONY: messages
messages:
	uv run django-admin makemessages -l fr --ignore=manage.py,docs/*
	@make deprecation-warning

.PHONY: compilemessages
compilemessages:
	uv run django-admin compilemessages
	@make deprecation-warning

.PHONY: quality
quality:
	uv run pre-commit run --all-files
	@make deprecation-warning

.PHONY: runserver
runserver:
	uv run python manage.py runserver $(local_port)
	@make deprecation-warning

.PHONY: test
test:
	uv run python manage.py test
	@make deprecation-warning

.PHONY: update_dsfr
update_dsfr:
	bash scripts/download_latest.sh
	uv run python manage.py trim_dist
	uv run python manage.py integrity_checksums
	uv run python manage.py make_icon_picker_files
	make collectstatic
	@make deprecation-warning

.PHONY: upgrade
upgrade:
    uv lock --upgrade
	uv run pre-commit autoupdate
	@make deprecation-warning

.PHONY: static_server
static_server:
	python -m http.server 1$(local_port) -d docs/
	@make deprecation-warning

.PHONY: export_static
export_static:
	uv run python manage.py migrate
	uv run python manage.py import_sample_data
	uv run python manage.py distill-local docs --force --collectstatic
	uv run python manage.py export_json
	@make deprecation-warning
