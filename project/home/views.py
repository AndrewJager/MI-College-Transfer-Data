from flask import render_template, Blueprint
from flask_login import current_user

home_blueprint = Blueprint(
    'home', __name__,
    template_folder = 'templates'
)

@home_blueprint.route('/')
def home():
    user = current_user
    return render_template('index.html', user=user)