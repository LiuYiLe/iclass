# coding: utf-8

from leancloud import Object

class Course(Object):
	""" course info """

	@property
	def title(self):
	    return self.get('title')

	@title.setter
	def title(self, title):
		return self.set('title', title)

	@property
	def info(self):
	    return self.get('info')

	@info.setter
	def info(self, info):
		return self.set('info', info)

	@property
	def time(self):
	    return self.get('time')

	@time.setter
	def time(self, time):
		return self.set('time', time)

	@property
	def location(self):
	    return self.get('location')

	@location.setter
	def location(self, location):
		return self.set('location', location)

	@property
	def mode(self):
		# course mode, YUE=0 / QIU=1
	    return self.get('mode')

	@mode.setter
	def mode(self, mode):
		return self.set('mode', mode)

	@property
	def user(self):
	    return self.get('user')

	@user.setter
	def user(self, user):
		return self.set('user', user)
