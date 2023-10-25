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
checkstyle:
	poetry run ruff check .

runserver:
	poetry run python manage.py runserver $(local_port)

update_dsfr:
	bash scripts/download_latest.sh
	poetry run python manage.py trim_dist
	poetry run python manage.py integrity_checksums
	poetry run python manage.py collecstatic --noinput
