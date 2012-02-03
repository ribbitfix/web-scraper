from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
	print "in the command"

	def handle_noargs(self):
		print "in the handle method"
