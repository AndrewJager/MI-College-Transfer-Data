from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object(os.environ['APP_SETTINGS'])
bcryptObj = Bcrypt(app)
localSystem = None

db = SQLAlchemy(app)

from project.home.views import home_blueprint
from project.user.views import user_blueprint
from project.college.views import college_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(college_blueprint)

from project.models import User

login_manager.login_view = "user.login"

@login_manager.user_loader
def load_user(user_id):
    try:
        user = User.query.filter(User.id == int(user_id)).first()
    except:
        user = None
    return user