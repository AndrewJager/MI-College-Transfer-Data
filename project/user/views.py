from flask import flash, redirect, render_template, request, \
   url_for, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from project.user.form import LoginForm, RegisterForm
from project.models import User
from project import db, bcryptObj

user_blueprint = Blueprint(
    'user', __name__,
    template_folder='templates'
)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    user = current_user
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcryptObj.check_password_hash(user.password, request.form['password']):
                login_user(user)
                flash('You were logged in.')
                return redirect(url_for('home.home'))
            else:
                error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', user=user, form=form)


@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home'))


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    return "Registration currently disabled"
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.home'))
    return render_template('register.html', user=current_user, form=form)

