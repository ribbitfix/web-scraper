from django.core.management.base import NoArgsCommand
from pyquery import PyQuery
from webscraperApp.models import Topic, Link

class Command(NoArgsCommand):

	def handle_noargs(self, **options):

		# create list of topic links
		jQuery = PyQuery(url='http://www.longecity.org/forum/forum/399-townhall/')
		topics = []
		for t in jQuery('#forum_table td.col_f_content h4 a'):
			topics.append(jQuery(t).attr('href'))

		# for each topic, create Topic object and associated Link objects 
		for topic in topics:
			jQuery = PyQuery(url=topic)
			title = jQuery('h1.ipsType_pagetitle').html()
			topicLink = topic
			t = Topic.objects.create(title=title, topicLink=topicLink)
			for link in jQuery('div.entry-content a'):
				url = jQuery(link).attr('href')
				try:
					l = Link.objects.get(link=url)
				except Link.DoesNotExist:
					l = Link.objects.create(link=url)
				#l, created = Link.objects.get_or_create(link=url)
				#t.links.add(l)

				'''(This works, but the above is maybe better)				
				if Link.objects.filter(link=url).exists():
					l = Link.objects.filter(link=url)[0]
					l.topic.add(t)
				else:
					l = Link(topic=t, link=link)
					l.add()'''


				
