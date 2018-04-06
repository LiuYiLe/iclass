#coding:utf-8

from leancloud import User
from leancloud import Query
from leancloud import errors
import tornado.web
import hashlib
from models.userprofile import UserProfile

class authBase(tornado.web.RequestHandler):
   def get_current_user(self):
      return self.get_secure_cookie('username')

class staticData(authBase):
   def init(self):
      self.sitename = SITESETTINGS['site_name']
      self.siteversion = SITESETTINGS['site_version']
      self.signeduser = SignValidateBase.get_current_user(self)
      if self.session.query(User).filter(User.username == self.signeduser).first().luid == 1:
          self.write('<script language="javascript">alert("你不适合这里！！");self.location="/signin";</script>')

class logIn(authBase):
   def get(self):
      self.title = 'Log In'
      self.render('login.html')

   def post(self):
      username = self.get_argument('username', default='')
      password = self.get_argument('password', default='')
      #md5_psw = hashlib.md5(password).hexdigest()
      try:
          User().login(username, password)
          self.set_secure_cookie('username', username)
          self.redirect('/')
      except errors.LeanCloudError, e:
          print e
          self.write('<script language="javascript">alert("%s");self.location="/login";</script>' % str(e))

class logOut(authBase):
   def get(self):
      self.clear_cookie('username')
      self.redirect('/')

class signUp(authBase):
   def get(self):
      self.title = 'Sign Up'
      self.render('signup.html')

   def post(self):
      username = self.get_argument('username', default='')
      password = self.get_argument('password', default='')
      passvali = self.get_argument('passvali', default='')
      email = self.get_argument('email', default='')
      mobilePhoneNumber = self.get_argument('phone', default='')
      if password == passvali:
          try:
              user = User()
              user.set("username", username)
              user.set("password", password)
              user.set("email", email)
              user.set("mobilePhoneNumber", mobilePhoneNumber)
              user.sign_up()
              userProfile = UserProfile()
              userProfile_fields = ['user', 'realName', 'gender', 'school', 'grade', 'major', 'about', 'avatar']
              for key in userProfile_fields:
                  userProfile.set(key, "")
              userProfile.user = username
              userProfile.save()
              self.write('<script language="javascript">alert("注册成功");self.location="/login";</script>')
          except errors.LeanCloudError, e:
              self.write('<script language="javascript">alert("%s");self.location="/signup";</script>'% str(e))
