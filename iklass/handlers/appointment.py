#coding:utf-8

from leancloud import Object, Query, User, File, LeanCloudError
from models.userprofile import UserProfile
from models.course import Course
from home import globalBase
from auth import authBase
import tornado.locale

course_mode = {
    "appointment": "1",
    "demand": "0"
    }

class course0Base(globalBase):
    def initialize(self):
        super(course0Base, self).initialize()
        self.nav_item = 1

class listCourse(course0Base):
    def get(self):
        super(listCourse, self).initialize()
        self.title = '约课'
        courseList = Query(Course).equal_to("mode", course_mode["appointment"]).find()
        self.render('home_yue_list.html', courseList = courseList)
