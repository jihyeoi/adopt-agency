"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet
from forms import addPet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def list_pets():
    """List all the pets at the homepage"""

    pets = Pet.query.all()
    return render_template('pet-list.html', pets = pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    """displays a form to add a pet"""

    form = addPet()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        return redirect("/")

    else:
        return render_template("pet-add.html", form=form)
