from django.core.management.base import NoArgsCommand
from pyquery import PyQuery
from webscraperApp.models import TopicTitle, TopicLink

class Command(NoArgsCommand):

	def handle_noargs(self, **options):

		# create list of topic links
		jQuery = PyQuery(url='http://www.longecity.org/forum/forum/399-townhall/')
		topics = []
		for t in jQuery('#forum_table td.col_f_content h4 a'):
			topics.append(jQuery(t).attr('href'))

		# for each topic, get topic title and posted links 
		for topic in topics:
			jQuery = PyQuery(url=topic)
			title = jQuery('h1.ipsType_pagetitle').html()
			t = TopicTitle(title=title)
			t.save()
			for link in jQuery('div.entry-content a'):
				url = jQuery(link).attr('href')
				l = TopicLink(topicTitle=t, link=url)
				l.save()