"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL

# TODO: add form at the end of the name
class AddPet(FlaskForm):
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

    age = SelectField(
        "Age Category",
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')])

    notes = StringField("Notes")


# TODO: add form at the end of the name
class EditPet(FlaskForm):
    """form for editing pets"""

    photo_url = StringField(
        "Photo Url",
        validators=[Optional(), URL()])

    notes = StringField("Notes")

    available = BooleanField("Availability")




