from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class ZipcodeForm(FlaskForm):
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    submit = SubmitField('Get Weather')