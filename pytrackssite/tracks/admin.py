from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin  	# Provides Markdownx model admin functionality.
from .models import Track, Tutorial  				# Provides app models.


admin.site.register(Track, MarkdownxModelAdmin)  		# Registers Track model for admin module.
admin.site.register(Tutorial, MarkdownxModelAdmin)  	# Registers Tutorial model for admin module.
