#!/usr/bin/env python

import os       # Needed for setting environment
import sys      # Needed for setting the path
import django   # Needed for Django project interaction

# Set the path so that Django can find the settings file.
sys.path.append('.')
# Set the settings file to pytrackssite.settings.
os.environ['DJANGO_SETTINGS_MODULE'] = 'pytrackssite.settings'

# Run django setup function.
django.setup()

# Import the User model
from django.contrib.auth.models import User  # noqa

# Query for the admin user, set the password and save the user.
admin_user = User.objects.get(username='admin')
admin_user.set_password('admin')
admin_user.save()
