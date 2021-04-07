#!/usr/bin/env bash

# Get command line options
OPTS=$@

# Run the manage runserver task with options.
python manage.py runserver $OPTS
