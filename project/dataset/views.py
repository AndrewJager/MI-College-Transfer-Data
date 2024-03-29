from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import login_required, current_user

from project.dataset.form import DatasetForm
from project.models import Dataset, College
from project import db

dataset_blueprint = Blueprint(
    'dataset', __name__,
    template_folder='templates'
)

@dataset_blueprint.route('/new_data', methods=['GET', 'POST'])
@login_required
def newDataset():
    user = current_user
    form = DatasetForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            dataset = Dataset()
            dataset.college_id = form.college.data.id   
            dataset.accept_transfer = form.acceptTransfers.data
            dataset.year = form.year.data
            dataset.transfer_applicants = form.applied.data
            dataset.transfer_admitted = form.admitted.data
            dataset.transfer_enrolled = form.enrolled.data
            dataset.reference = form.reference.data

            db.session.add(dataset)
            db.session.commit()
            return redirect(url_for('home.home'))
        else:
            print(form.errors)

    return render_template('edit_dataset.html', user=user, form=form)

@dataset_blueprint.route('/edit_dataset/<string:id>', methods=['GET', 'POST'])
@login_required
def editDataset(id):
    user = current_user
    form = DatasetForm(request.form)
    dataset = Dataset.query.filter_by(id=id).first()

    if request.method == 'GET':
        form.college.data = College.query.filter_by(id=dataset.college_id).first()
        form.acceptTransfers.data = dataset.accept_transfer
        form.year.data = dataset.year
        form.applied.data = dataset.transfer_applicants
        form.admitted.data = dataset.transfer_admitted
        form.enrolled.data = dataset.transfer_enrolled
        form.reference.data = dataset.reference
        form.totalEnrollment.data = dataset.total_enrollment
        form.minTransferGrade.data = dataset.min_transfer_grade
        form.maxCredits2Yr.data = dataset.max_credits_2yr
        form.maxCredits4Yr.data = dataset.max_credits_4yr

    if request.method == 'POST':
        if form.validate_on_submit():
            #dataset.college_id = form.college.data.id   
            dataset.accept_transfer = form.acceptTransfers.data
            dataset.year = form.year.data
            dataset.transfer_applicants = form.applied.data
            dataset.transfer_admitted = form.admitted.data
            dataset.transfer_enrolled = form.enrolled.data
            dataset.reference = form.reference.data
            dataset.total_enrollment = form.totalEnrollment.data
            dataset.min_transfer_grade = form.minTransferGrade.data
            dataset.max_credits_2yr = form.maxCredits2Yr.data
            dataset.max_credits_4yr = form.maxCredits4Yr.data

            db.session.commit()
            return redirect(url_for('home.home'))
        else:
            print(form.errors)

    return render_template('edit_dataset.html', user=user, form=form)

@dataset_blueprint.route('/data/<string:id>')
def viewDataset(id):
    user = current_user
    dataset = Dataset.query.filter_by(id=id).first()
    college = College.query.filter_by(id=dataset.college_id).first()
    return render_template('view_dataset.html', user=user, dataset=dataset, col=college)