from django.contrib import admin
from .models import Article, Link


admin.site.register(Article)  # Registers Article model for admin module.
admin.site.register(Link)     # Registers Link model for admin module.
