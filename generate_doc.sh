#!/bin/bash
mkdir docs
poetry run python manage.py collectstatic --noinput
poetry run python manage.py distill-local docs --force
touch docs/.nojekyll
mv docs/django-dsfr/* docs/
rmdir docs/django-dsfr
