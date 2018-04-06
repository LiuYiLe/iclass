# coding: utf-8

from leancloud import Object

class UserProfile(Object):
	""" user info """

	@property
	def user(self):
	    return self.get('user')

	@user.setter
	def user(self, user):
		return self.set('user', user)

	@property
	def realName(self):
	    return self.get('realName')

	@realName.setter
	def realName(self, name):
		return self.set('realName', name)

	@property
	def gender(self):
	    return self.get('gender')

	@gender.setter
	def gender(self, gender):
		return self.set('gender', gender)

	@property
	def school(self):
	    return self.get('school')

	@school.setter
	def school(self, school):
		return self.set('school', school)

	@property
	def grade(self):
	    return self.get('grade')

	@grade.setter
	def grade(self, major):
		return self.set('grade', grade)

	@property
	def major(self):
	    return self.get('major')

	@major.setter
	def major(self, major):
		return self.set('major', major)

	@property
	def about(self):
	    return self.get('about')

	@about.setter
	def about(self, about):
		return self.set('about', about)

	@property
	def avatar(self):
	    return self.get('avatar')

	@avatar.setter
	def avatar(self, avatar):
		return self.set('avatar', avatar)
