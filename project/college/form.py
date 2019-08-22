from flask_wtf import Form 
from wtforms import TextField, SelectField
from wtforms.validators import DataRequired

from constants import collegeTypes

class CollegeForm(Form):
    collegeName = TextField('collegeName', validators=[DataRequired()])
    collegeType = SelectField('collegeType', 
        choices=[(colType, colType) for colType in collegeTypes])

