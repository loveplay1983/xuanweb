# _*_ coding: utf-8 _*_

"""
 author: Xiong Min Xuan
 study, study, and study!!!
"""

import os
import sys

import click

from flask import Flask
from flask import redirect, url_for, abort, render_template, flash

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired

# SQLite URI compatible
WIN = sys.platform.startswith("win")
if WIN:
    prefix = "sqlite:///"  # windows
else:
    prefix = "sqlite:////"  # unix-like

app = Flask(__name__)
# Left and right whitespace removal
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "secret string")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", prefix + os.path.join(app.root_path, "data.db"))
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)


# Handlers
@app.shell_context_processors
def make_shell_context():
    return dict(db=db, Note=Note, Author=Author, Article=Article, \
                Writer=Writer, Book=Book, Singer=Singer, SOng=Song, \
                Citizen=Citizen, City=City, Capital=Capital, \
                Country=Country, Teacher=Teacher, Student=Student, \
                Post=Post, Comment=Comment, Draft=Draft)


@app.cli.command()
@click.option("--drop", is_flag=True, help="Create after drop.")
def initdb(drop):
    """
    Initialize the database.
    """
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("Database is initialized.")


# Forms
class NewNoteForm(FlaskForm):
    body = TextAreaField("Body", validators=[DataRequired()])
    submit = SubmitField("Save")


class EditNoteForm(FlaskForm):
    body = TextAreaField("Body", validators=[DataRequired()])
    submit = SubmitField("Update")


class DeleteNoteForm(Flask):
    submit = SubmitField("Delete")


# Models - Tables
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)

    # optional
    def __repr__(self):
        return "<Note {0!r}>".format(self.body)


# routes and view functions
@app.route("/")
def index():
    form = DeleteNoteForm()
    notes = Note.query.all()
    return render_template("index.html", notes=notes \
                           , form=form)

@app.route("/new", methods=["GET", "POST"])
def new_note():
    form = NewNoteForm()
    if form.validate_on_submit():
