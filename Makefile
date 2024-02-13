run_app:
	flask --app riiran-app run --debug

run_with_gunicorn:
	gunicorn -w 4 --access-logfile=- --bind 0.0.0.0:8000 'riiran-app:create_app()'

.PHONY: run_app, run_with_gunicorn