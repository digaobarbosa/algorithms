__author__ = 'digao'
from google.appengine.ext import db

class Post(db.Model):
    title = db.StringProperty(verbose_name="Title", required=True)
    content = db.StringProperty(required=True,verbose_name='Content', multiline=True)
    insert_date = db.DateTimeProperty(auto_now_add=True,verbose_name='Insert date')

class MyUser(db.Model):
    name = db.StringProperty(verbose_name="Name", required=True)
    hash = db.StringProperty(verbose_name="Name", required=True)
    email = db.StringProperty(verbose_name="Name", required=False)
