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

            db.session.add(dataset)
            db.session.commit()
            return redirect(url_for('home.home'))
        else:
            print(form.errors)


    return render_template('edit_dataset.html', user=user, form=form)