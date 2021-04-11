from django.contrib.auth.models import User  	# For User model
from django.db import models  					# For model classes
from markdownx.models import MarkdownxField  	# Adds a Markdown editor field


class Track(models.Model):
	""" A track is a set of tutorials for a given purpose. """
	name = models.CharField('Name', max_length=255, unique=True)  	# Name of track
	description = MarkdownxField('Description')						# Description of the track
	created = models.DateTimeField(auto_now_add=True)  				# Created datetime of track
	modified = models.DateTimeField(auto_now=True)  				# Last modified datetime of track
	owner = models.ForeignKey(User, on_delete=models.CASCADE)		# Owner of track

	def __str__(self):
		return f'{self.name}'


class Tutorial(models.Model):
	""" A tutorial is an article for a given sub-purpose for a track. """
	name = models.CharField('Name', max_length=255)					# Name of tutorial
	track = models.ForeignKey(Track, on_delete=models.CASCADE)		# Related track
	description = MarkdownxField('Description')						# Description of the tutorial
	created = models.DateTimeField(auto_now_add=True)  				# Created datetime of tutorial
	modified = models.DateTimeField(auto_now=True)  				# Last modified datetime of tutorial
	owner = models.ForeignKey(User, on_delete=models.CASCADE)		# Owner of tutorial
	parent = models.ForeignKey(										# Related last tutorial in track series
		'self', on_delete=models.CASCADE, null=True, blank=True
	)

	class Meta:
		unique_together = (
			('name', 'track'),
		)

	def __str__(self):
		return f'{self.name}'
