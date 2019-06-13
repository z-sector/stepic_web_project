sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE qadb;"
mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'pass123';"
mysql -uroot -e "GRANT ALL ON qadb.* TO 'django'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"

cd ask
python manage.py makemigrations
python manage.py migrate

