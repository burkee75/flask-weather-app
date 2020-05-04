from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class ZipcodeForm(FlaskForm):
    zipcode = StringField('Zipcode', validators=[
        DataRequired(),
        Length(min=5, max=5, message='Zipcode must be 5 digits long')])
    submit = SubmitField('Get Weather')
