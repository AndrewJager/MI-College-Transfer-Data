from flask import render_template, Blueprint
from flask_login import current_user

from project import db
from project.models import College

home_blueprint = Blueprint(
    'home', __name__,
    template_folder = 'templates'
)

@home_blueprint.route('/')
def home():
    user = current_user
    colleges = db.session.query(College).all()
    return render_template('index.html', user=user, colleges=colleges)