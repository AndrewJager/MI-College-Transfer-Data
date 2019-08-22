# sandbox for database stuff

from project import db
from project.models import *

user = db.session.query(User).first()
user.is_admin = True

db.session.commit()