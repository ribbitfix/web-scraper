from django.db import models

class Topic(models.Model):
	title = models.CharField(max_length=200)
	topicLink = models.URLField()
	links = models.ManyToManyField("Link")

	def __unicode__(self):
		return self.title

class Link(models.Model):
	link = models.URLField(unique=True)

	def __unicode__(self):
		return self.link
