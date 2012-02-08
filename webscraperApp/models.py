from django.db import models

class Topic(models.Model):
	title = models.CharField(max_length=200)
	topicLink = models.URLField()

	def __unicode__(self):
		return self.title

class Link(models.Model):
	topic = models.ForeignKey(Topic)
	link = models.URLField(unique=True)

	def __unicode__(self):
		return self.link
