from google.appengine.ext import webapp
from google.appengine.ext.webapp import  template
from domain import MyUser
import hashlib
from domain import MyUser
SECRET='sudoMake'


form = """
<form action="/testform" method="get">

<input name="q">
    <input type="submit">
</form>
"""

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(form)

rot = """
<form action="/testform" method="post">
    <textarea style="width:420px;height:300px;"name="text">%s</textarea><br>
    <input type="submit">
</form>
"""
ROT = 'abcdefghijklmnopqrstuvwxyz'
import cgi
class Teste(webapp.RequestHandler):

    def rotate(self,s):
        def toLetter(c):
            if c.isalpha():
                return c.lower()==c and ROT[(ROT.index(c.lower())+13)%26] or ROT[(ROT.index(c.lower())+13)%26].capitalize()
            else:
                return c
        return "".join( [toLetter(c) for c in s])
    def get(self):
        self.response.out.write(rot%"")

    def post(self):
        text = self.request.get('text')
        self.response.out.write(rot%cgi.escape(self.rotate(text),True))


import os,re

class Logout(webapp.RequestHandler):
    def get(self):
        self.response.headers.add_header('Set-Cookie','userid=; Path=/')
        self.redirect('/signup')

class Login(webapp.RequestHandler):
    temp_path = os.path.join('templates','login.html')

    def get(self):
        self.response.out.write(template.render(Login.temp_path,{'username':''},True))

    def post(self):
        username = self.request.get('username')
        passw = self.request.get('password')
        temp_vs = {'username':username}
        resp = MyUser.gql("WHERE name=:1",username).get()
        if resp:
            user = resp
            if user.hash==passw:
                create_cookie(self.response,user)
                self.redirect('/welcome')
            else:
                temp_vs['login_error']='Invalid login'
                self.response.out.write(template.render(Login.temp_path,temp_vs,True))






class SignUp(webapp.RequestHandler):


    temp_path = os.path.join('templates','signup.html')
    def get(self):
        self.response.out.write(template.render(SignUp.temp_path,{'username':'','email':''},True))

    def post(self):
        username = self.request.get('username')
        email = self.request.get('email')
        passw = self.request.get('password')
        verify = self.request.get('verify')
        temp_vs = {'username':username,
                   'email':email}

        if not re.match(r"^[a-zA-Z0-9_-]{3,20}$",username):
            temp_vs['username_error']="Username invalid"
        count = MyUser.gql("WHERE name=:1",username).count()
        if count:
            temp_vs['username_error']="Username occupied"
        if not re.match(r'^.{3,20}$',passw):
            temp_vs['password_error']="Invalid password"
        if not (email=='' or re.match(r'^[\S]+@[\S]+\.[\S]+$',email)):
            temp_vs['email_error']="invalid email"
        if verify!= passw:
            temp_vs['verify_error']="passes dont match"
        if len(temp_vs)>2:
            self.response.out.write(template.render(SignUp.temp_path,temp_vs,True))
        else:
            user = MyUser(name=username,hash=passw,email=email)
            user.save()
            id = user.key().id()
            self.response.headers.add_header('Set-Cookie','userid='+encode_cookie(id)+"; Path=/")
            self.redirect('/welcome')


def encode_cookie(s):
    return '%s|%s'%(str(s),hashlib.sha256(str(s)+SECRET).hexdigest())

def decode_cookie(s):
    if not s:
        return None
    v,h = s.split('|')
    h2 = encode_cookie(v)
    if h2==s:
        return v
    return None

def create_cookie(response,user):
        id = user.key().id()
        response.headers.add_header('Set-Cookie','userid='+encode_cookie(id)+"; Path=/")

class Welcome(webapp.RequestHandler):
    temp_path = os.path.join('templates','welcome.html')
    def get(self):
        userid = decode_cookie(self.request.cookies['userid'])
        username = 'Anonymous'
        if userid:
            user = MyUser.get_by_id(int(userid))
            username = user.name
        self.response.out.write(template.render(Welcome.temp_path,{'username':username}))

import domain

class Permalink(webapp.RequestHandler):
    temp_path = os.path.join('templates','blog.html')
    def get(self,id):
        one = domain.Post.get(id)
        self.response.out.write(template.render(Permalink.temp_path,{'list': (one,)}))



class PostHandler(webapp.RequestHandler):
    temp_path = os.path.join('templates','newpost.html')
    def get(self):
        self.response.out.write(template.render(PostHandler.temp_path,{}))
    def post(self):
        title  = self.request.get('subject')
        content = self.request.get('content')
        error =False
        model = {title:title,content:content}
        if not content:
            model['content_error'] = 'Cant be empty'
            error = True
        if not title:
            model['title_error'] = 'Cant be empty'
            error = True
        if error:
            self.response.out.write(template.render(PostHandler.temp_path,model))
            return

        one = domain.Post(title=title,content=content)
        one.save()
        self.redirect('/blog/'+str(one.key()))


class Blog(webapp.RequestHandler):
    temp_path = os.path.join('templates','blog.html')
    def get(self):
        list = domain.Post.all()
        self.response.out.write(template.render(Blog.temp_path,{'list':list}))

app = webapp.WSGIApplication([('/', MainHandler),('/testform',Teste),('/signup',SignUp),('/welcome',Welcome),
    ('/blog',Blog),('/blog/newpost',PostHandler),('/blog/(.+)',Permalink),('/login',Login),('/logout',Logout)],

                             debug=True)

