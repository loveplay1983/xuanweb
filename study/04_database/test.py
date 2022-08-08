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


# Models - database table
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)

    # optional
    def __repr__(self):
        return "<Note {0!r}>".format(self.body)


# one - many
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    phone = db.column(db.String(20))
    articles = db.relationship("Article")

    def __repr__(self):
        return "<Author {0!r}>".format(self.name)


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
        """
        Write content into to the database 
        if there exists valid input data, 
        then return back to index page
        """
        body = form.body.data  # Generate text body from form input
        note = Note(body=body)  # Pass the text data to model
        db.session.add(note)  # Write the data into database
        db.session.commit()
        flash("Your note is saved.")
        return redirect(url_for("index"))
    # Display the new_note page
    return render_template("new_note.html", form=form)


@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    form = EditNoteForm()
    note = Note.query.get(note_id)
    if form.validate_on_submit():
        note.body = form.body.data
        db.session.commit()
        flash("Your note is updated.")
        return redirect(url_for("index"))
    form.body.data = note.body  # Preset or display the current note
    return render_template("edit_note.html", form=form)


@app.route("/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    form = DeleteNoteForm()
    if form.validate_on_submit():
        note = Note.query.get(note_id)
        db.session.delete(note)
        db.session.commit()
        flash("Your note is deleted.")
    else:
        abort(400)
    return redirect(url_for("index"))


@app.route("")
