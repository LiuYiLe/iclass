# coding=utf-8
__author__ = 'JIE'

import tornado.ioloop
import tornado.wsgi
import os
from urls import urls, ui_modules

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "gzip": True,
    "debug": True,
    "cookie_secret": "dEr2Viz6TrqsoQVbQCRdxUmzKB5q40U0jYtp+fnsAOY=",
    "login_url": "/login",
    "xsrf_cookies": True,
    "ui_modules": ui_modules
}

app = tornado.wsgi.WSGIApplication(urls, **settings)




# if __name__ == "__main__":
#     app.listen(8888)
#     print 'server start'
#     tornado.ioloop.IOLoop.current().start()
