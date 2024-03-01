"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import InputRequired, Optional, URL

class addPet(Flaskform):
    """form for adding pets"""

    name = StringField(
        "Pet name",
        validators=[InputRequired()])

    species = SelectField(
        "Species",
        choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])

    photo_url = StringField(
        "Photo Url",
        validators=[Optional(), URL()])

    age = IntegerField("Age in years")

    notes = StringField("Notes")