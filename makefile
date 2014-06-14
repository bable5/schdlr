rebuild:
	sudo fig kill
	sudo fig rm --force
	rm backend/db*
	sudo fig run backend python manage.py syncdb
	sudo fig up backend
