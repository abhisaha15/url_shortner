import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    rid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),unique= True)
    email = db.Column(db.String(100),unique= True)
    password = db.Column(db.String(20))
    dob = db.Column(db.String(15))

    def __int__(self,unm,uem,pas,dob):
        self.username = unm
        self.email = uem
        self.password = pas
        self.dob = dob



class Url(db.Model):
    __tablename__ = 'url'
    rid = db.Column(db.Integer, primary_key=True)
    url_name = db.Column(db.String, nullable=False)
    url_short_name = db.Column(db.String, unique=True, nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.rid'))
    creation_date = db.Column(db.DateTime,nullable=False, default=datetime.datetime.now())

    def __int__(self,unm,usnm,onr):
        self.url_name = unm
        self.url_short_name = usnm
        self.owner = onr











