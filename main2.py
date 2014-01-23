from google.appengine.ext import webapp
from google.appengine.ext.webapp import  template


import cgi
import os,re
import domain

class Welcome(webapp.RequestHandler):

    temp_path = os.path.join('templates','welcome.html')
    def get(self):
        self.response.out.write(template.render(Welcome.temp_path,{'username':self.request.get('user')}))


app = webapp.WSGIApplication([('/',Welcome)],

                             debug=True)

