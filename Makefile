runserver:
	poetry run python manage.py runserver 8765

update_dsfr:
	bash scripts/download_latest.sh
	poetry run python manage.py trim_dist
	poetry run python manage.py integrity_checksums
