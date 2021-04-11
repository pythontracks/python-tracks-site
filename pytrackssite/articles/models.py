from django.contrib.auth.models import User  # Handles site users
from django.db import models  # Handles model classes


class Link(models.Model):
	"""
	Content link for articles.
	"""
	name = models.CharField('Name', max_length=255)  	# Name of content link
	link = models.URLField()  							# Content link (URL)

	def __str__(self):
		return f'{self.name}: {self.link}'


class Article(models.Model):
	"""
	Article model for articles and posts that will show up
	in main site.
	"""
	title = models.CharField('Title', max_length=255, unique=True)    		# Article title
	description = models.TextField('Description', null=True, blank=True)  	# Article summary/description
	author = models.ForeignKey(User, on_delete=models.CASCADE)  			# Author user
	content = models.TextField('Content')  									# Content for article
	created = models.DateTimeField(auto_now_add=True)  						# Creation datetime for article
	modified = models.DateTimeField(auto_now=True)  						# Last modified datetime for article

	def __str__(self):
		return f'{self.title}'
