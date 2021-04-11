from django.contrib import admin
from .models import Track, Tutorial


admin.site.register(Track)  	# Registers Track model for admin module.
admin.site.register(Tutorial)  	# Registers Tutorial model for admin module.
