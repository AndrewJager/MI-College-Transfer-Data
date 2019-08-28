from project import db, bcryptObj
import bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, password):
        self.name = name
        pwhash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        self.password = pwhash.decode('utf8')
        self.isAdmin = False
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class College(db.Model):
    __tablename__ = "colleges"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    college_type = db.Column(db.String) # 2-year, 4-year, masters, ect
    college_ownership = db.Column(db.String) # public, private non-profit, private for-profit, ect
    founded = db.Column(db.Integer)
    xPosition = db.Column(db.Integer)
    yPosition = db.Column(db.Integer)
    datasets = relationship("Dataset")

    def getMapColor(self):
        if self.college_type == 'N/A':
            color = 'grey'
        if self.college_type == "Associate's college":
            color = "red"
        if self.college_type == "Baccalaureate college":
            color = 'green'
        if self.college_type == "Master's university":
            color = 'red'
        if self.college_type == "Research university":
            color = 'black' 
        if self.college_type == "Special-focus institution":
            color = 'silver' 


class Dataset(db.Model):
    __tablename__ = "datasets"

    id = db.Column(db.Integer, primary_key=True)
    college_id = db.Column(db.Integer, ForeignKey('colleges.id'))
    year = db.Column(db.String)
    accept_transfer = db.Column(db.Boolean)