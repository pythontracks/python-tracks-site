#!/usr/bin/env bash

### resetdb.sh is a development tool. It is used for resetting the database until we get the project to a general
### working state that has the minimal expected functionality.

# Set database name.
DBNAME="pytrackssite"

# Set database owner.
DBUSER="admin"

# Set Django admin username.
DJADMIN="admin"

# Set Django admin email.
DJADMIN_EMAIL="admin@localhost"

# Drop database.
sudo su - postgres -c "dropdb $DBNAME"

# Recreate database.
sudo su - postgres -c "createdb $DBNAME -O $DBUSER"

# Clear migrations
rm -rf core/migrations
rm -rf articles/migrations
rm -rf tracks/migrations

# Make migrations
python manage.py makemigrations core
python manage.py makemigrations articles
python manage.py makemigrations tracks

# Run Django migrate script.
python manage.py migrate

# Run createsuperuser.
python manage.py createsuperuser --username $DJADMIN --email $DJADMIN_EMAIL --noinput

# Run Python script to set the superuser's password.
python scripts/setadminpw.py
