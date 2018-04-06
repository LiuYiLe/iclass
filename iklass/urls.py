#coding:utf-8

from handlers import home, auth, exception, profile, appointment
from module import navbarModule

urls = [
    ("/", home.Home),
#auth
    ("/login", auth.logIn),
    ("/logout", auth.logOut),
    ("/signup", auth.signUp),
#appointment
    ("/appointment", appointment.listCourse),
#profile
    (r"/user/([0-9a-zA-Z]*)", profile.showProfile),
    (r"/user/([0-9a-zA-Z]*)/profile", profile.editProfile),
    (r"/user/([0-9a-zA-Z]*)/new", profile.newCourse),
#exception
    (r".*", exception.errorHandler)
]

ui_modules = {
    'navbar': navbarModule,
}
