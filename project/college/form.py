from flask_wtf import Form 
from wtforms import TextField, SelectField, IntegerField
from wtforms.validators import DataRequired

from constants import collegeTypes, collegeOwnerships

class CollegeForm(Form):
    collegeName = TextField('collegeName', validators=[DataRequired()])
    collegeType = SelectField('collegeType', 
        choices=[(colType, colType) for colType in collegeTypes])
    collegeOwnership = SelectField('collegeOwner', 
        choices=[(colOwner, colOwner) for colOwner in collegeOwnerships])
    founded = IntegerField('founded')
    xPosition = IntegerField('xPosition')
    yPosition = IntegerField('yPosition')

