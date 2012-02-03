class Topic:
	def __init__(self, title):
		self.title = title
		self.links = []
	def add_link(self, link):
		self.links.append(link)
