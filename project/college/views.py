from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import login_required, current_user

from project.college.form import CollegeForm
from project.models import College
from project import db

college_blueprint = Blueprint(
    'college', __name__,
    template_folder='templates'
)

@college_blueprint.route('/new_college', methods=['GET', 'POST'])
@login_required
def newCollege():
    user = current_user
    form = CollegeForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            college = College()
            college.name = form.collegeName.data
            college.college_type = form.collegeType.data 

            db.session.add(college)
            db.session.commit()
            return redirect(url_for('home.home'))

    return render_template('edit_college.html', user=user, form=form)
