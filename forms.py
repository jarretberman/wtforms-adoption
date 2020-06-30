from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional, URL, AnyOf


class PetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField('Pet Name', validators = [InputRequired()])
    species = StringField('Species', validators = [InputRequired(), AnyOf(values=['dog','cat','porcupine'],message = 'We only accept dogs, cats, or porcupines')])
    photo_url = StringField('Photo', validators =[Optional(),URL()])
    age = FloatField('Age')
    notes = StringField('Notes')

