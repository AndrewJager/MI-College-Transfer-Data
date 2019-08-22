# sandbox for database stuff

from project import db
from project.models import *

user = db.session.query(User).first()
user.isAdmin = True
db.session.add(user)

db.session.commit()