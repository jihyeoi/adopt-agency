"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet
from forms import AddPet, EditPet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.debug = False

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

    form = AddPet()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species,
        photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template("pet-add.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def pet_profile_edit(pet_id):
    """displays the pet's profile and has a form to edit the profile"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPet(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()

        return redirect("/")

    else:
        return render_template("pet-profile.html", form=form, pet=pet)
