# coding: utf-8

from leancloud import Object

class Event(Object):
	""" Activity info """

	@property
	def title(self):
	    return self.get('title')

	@title.setter
	def title(self, title):
		return self.set('title', title)

	@property
	def link(self):
	    return self.get('link')

	@link.setter
	def link(self, link):
		return self.set('link', link)

	@property
	def image(self):
	    return self.get('image')

	@image.setter
	def image(self, image):
		return self.set('image', image)
