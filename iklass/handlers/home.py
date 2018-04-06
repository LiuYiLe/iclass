#coding:utf-8

import tornado.web
from leancloud import Query
from leancloud import User
from leancloud import errors
from auth import authBase
from models.userprofile import UserProfile

class TestHander(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")
'''
class homeBase(SignValidateBase):
    def init(self):
        self.sitename = SITESETTINGS['site_name']
        self.siteversion = SITESETTINGS['site_version']
        self.session = db_session.getSession
        self.signeduser = SignValidateBase.get_current_user(self)
        if self.signeduser:
            self.user = self.session.query(User).filter(User.username == self.signeduser).first()
            self.signedid = self.user.uid
            self.signavatar = self.user.uavatar
        else:
            self.signedid = None
'''
class globalBase(authBase):
    def initialize(self):
        self.currentUser = Query(UserProfile).equal_to("user", self.current_user).first()
        self.nav_item = -1

class Home(globalBase):
    def get(self):
        #globalBase.initialize(self)
        super(Home, self).initialize()
        #self.currentUser = Query(UserProfile).equal_to("user", self.current_user).first()
        self.nav_item = 0
        #super(home, self).init(self)
        self.title = '爱上课-人人皆老师'
        self.render('home_index.html')
