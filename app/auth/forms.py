from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo

class UserCreationForm(FlaskForm):
    poke_name = StringField('Pokemon Name', validators=[])
    submit = SubmitField()