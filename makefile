rebuild:
	sudo fig kill
	sudo fig rm --force
	- rm backend/db*
	sudo fig build backend
	sudo fig run backend python manage.py syncdb --noinput
	sudo fig run backend python manage.py stock_data
	sudo fig up backend

deploy:
	./deploy.sh
