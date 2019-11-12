from flask_wtf import FlaskForm 
from wtforms import TextField, SelectField, IntegerField, BooleanField, StringField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from constants import datasetYears
from project.models import College

class DatasetForm(FlaskForm):
    year = SelectField('year', 
        choices=[(year, year) for year in datasetYears], validators=[DataRequired()])
    college = QuerySelectField(query_factory=lambda: College.query.all(), get_label='name')

    acceptTransfers = BooleanField('acceptTransfers')
    applied = IntegerField('applied', validators=[DataRequired()])
    admitted = IntegerField('admitted', validators=[DataRequired()])
    enrolled = IntegerField('enrolled', validators=[DataRequired()])
    reference = StringField('reference', validators=[DataRequired()])
    totalEnrollment = IntegerField('totalEnrollment', validators=[DataRequired()])
    minTransferGrade = StringField('minTransferGrade', validators=[DataRequired()])
    maxCredits2Yr = IntegerField('maxCredits2Yr', validators=[DataRequired()])
    maxCredits4Yr = IntegerField('maxCredits4Yr', validators=[DataRequired()])