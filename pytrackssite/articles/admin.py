from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin  	# Provides Markdownx model admin functionality.
from .models import Article, Link  					# Provides app models.


admin.site.register(Article, MarkdownxModelAdmin)  	# Registers Article model for admin module.
admin.site.register(Link)     						# Registers Link model for admin module.
