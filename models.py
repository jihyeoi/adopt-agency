"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

# TODO: make notes not nullable, add default = ""
class Pet(db.Model):
    """model for pet"""

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True)

    name = db.Column(
        db.String(50),
        nullable=False)

    species = db.Column(
        db.String(50),
        nullable=False)

    photo_url = db.Column(
        db.Text,
        nullable=False,
        default='')

    age = db.Column(
        db.Text,
        nullable=False)

    notes = db.Column(
        db.Text)

    available = db.Column(
        db.Boolean,
        default=True)