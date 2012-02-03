from django.db import models

class TopicTitle(models.Model):
	title = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title

class TopicLink(models.Model):
	topicTitle = models.ForeignKey(TopicTitle)
	link = models.URLField()

	def __unicode__(self):
		return self.link
