#coding:utf-8

from leancloud import Object, Query, User, File, LeanCloudError
from models.userprofile import UserProfile
from models.course import Course
from home import globalBase
from auth import authBase
import tornado.locale

class profileBase(globalBase):
    def initialize(self):
        super(profileBase, self).initialize()
        self.profile_mode = 0

class showProfile(profileBase):
    def get(self, username):
        super(showProfile, self).initialize()
        #self.profile_mode = 0
        str = '的主页'
        self.title = username + str.decode('utf8')
        try:
            user = Query(UserProfile).equal_to("user", username).first()
            self.render("home_page1.html", user = user, course_list = None)
        except LeanCloudError, e:
            pass

class editProfile(profileBase):
    def get(self, username):
        super(profileBase, self).initialize()
        #self.profile_mode = 0
        self.title = '编辑资料'
        try:
            user = Query(UserProfile).equal_to("user", username).first()
            self.render('home_page_profile.html', user = user)
        except LeanCloudError, e:
            pass

    def post(self, username):
        profile_fields = ['realName', 'gender', 'school', 'grade', 'major', 'about']
        userProfile = Query(UserProfile).equal_to("user", username).first()
        try:
            for key in profile_fields:
                userProfile.set(key, self.get_argument(key, ""))
                if 'file' in self.request.files:
                    file_dict_list = self.request.files['file']
                    for file_dict in file_dict_list:
                        data = file_dict["body"]
                        avatar = File("avatar", buffer(data))
                        avatar.save()
                userProfile.set("avatar", avatar.get_thumbnail_url(width='200', height='200'))
                userProfile.save()
                self.redirect('/user/'+username)
                print self.request
        except LeanCloudError, e:
            pass

class newCourse(profileBase):
    def get(self, username):
        super(profileBase, self).initialize()
        self.title = '发起新课程'
        try:
            user = Query(UserProfile).equal_to("user", username).first()
            self.render('home_page_request.html', user = user)
        except LeanCloudError, e:
            pass

    def post(self, username):
        course_fields = ['mode', 'title', 'info', 'time', 'location']
        course = Course()
        try:
            for key in course_fields:
                course.set(key, self.get_argument(key, ""))
            course.user = username
            course.save()
            self.redirect('user'+username)
        except LeanCloudError, e:
            pass
