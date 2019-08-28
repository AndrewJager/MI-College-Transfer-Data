from flask_wtf import FlaskForm 
from wtforms import TextField, SelectField, IntegerField, BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from constants import datasetYears
from project.models import College

class DatasetForm(FlaskForm):
    year = SelectField('year', 
        choices=[(year, year) for year in datasetYears], validators=[DataRequired()])
    college = QuerySelectField(query_factory=lambda: College.query.all(), get_label='name')
    acceptTransfers = BooleanField('acceptTransfers')