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
            college.college_ownership = form.collegeOwnership.data
            college.founded = form.founded.data 
            college.xPosition = form.xPosition.data   
            college.yPosition = form.yPosition.data

            db.session.add(college)
            db.session.commit()
            return redirect(url_for('home.home'))

    return render_template('edit_college.html', user=user, form=form)

@college_blueprint.route('/edit_college/<string:id>', methods=['GET', 'POST'])
@login_required
def editCollege(id):
    user = current_user
    form = CollegeForm(request.form)
    college = College.query.filter_by(name=id).first()
    if request.method == 'GET':
        form.collegeName.data = college.name
        form.collegeType.data = college.college_type
        form.collegeOwnership.data = college.college_ownership
        form.founded.data = college.founded
        form.xPosition.data = college.xPosition
        form.yPosition.data = college.yPosition

    if request.method == 'POST':
        college.name = form.collegeName.data
        college.college_type = form.collegeType.data 
        college.college_ownership = form.collegeOwnership.data
        college.founded = form.founded.data 
        college.xPosition = form.xPosition.data   
        college.yPosition = form.yPosition.data

        db.session.commit()
        return redirect(url_for('home.home'))

    return render_template('edit_college.html', user=user, form=form)

@college_blueprint.route('/college/<string:id>')
def viewCollege(id):
    user = current_user
    college = College.query.filter_by(name=id).first()
    return render_template('view_college.html', user=user, college=college)