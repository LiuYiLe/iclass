#coding:utf-8

import tornado.web

class navbarModule(tornado.web.UIModule):
    def render(self, currentUser, nav_item):
        return self.render_string("modules/navbar.html", currentUser = currentUser, nav_item = nav_item)

class profileModule(tornado.web.UIModule):
    pass
