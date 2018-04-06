#coding:utf-8

import tornado.web
from home import globalBase

class errorHandler(globalBase):
    def get(self):
        self.write_error(404)

    def write_error(self, status_code, **kwargs):
        self.title = str(status_code)
        if status_code == 404:
            self.render('404.html')
        elif status_code == 500:
            self.render('500.html')
        else:
            self.write('error:' + str(status_code))
