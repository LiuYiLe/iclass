# coding: utf-8

from leancloud import Object

class Comment(Object):
	""" course comment """

	@property
	def content(self):
	    return self.get('content')

	@content.setter
	def content(self, content):
		return self.set('content', content)

	@property
	def fromUid(self):
	    return self.get('fromUid')

	@fromUid.setter
	def fromUid(self, fromUid):
		return self.set('fromUid', fromUid)

	@property
	def toCid(self):
	    return self.get('toCid')

	@toCid.setter
	def toCid(self, toCid):
		return self.set('toCid', toCid)
