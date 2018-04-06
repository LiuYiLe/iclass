# coding: utf-8

from leancloud import Object

class Tag(Object):
	""" course tag info """

	@property
	def name(self):
	    return self.get('name')

	@name.setter
	def name(self, name):
		return self.set('name', name)
