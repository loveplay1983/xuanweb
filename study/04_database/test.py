# _*_ coding: utf-8 _*_

"""
 author: Xiong Min Xuan
 study, study, and study!!!
"""

from conf import app, db, initdb
from models import Note, Author, Article, Citizen, City, Country, \
    Capital, Student, Teacher, Writer, Book, Singer, Song, Comment, Post
from forms import NewNoteForm, EditNoteForm, DeleteNoteForm
from packages import redirect, url_for, abort, render_template, flash


# Handlers
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Note=Note, Author=Author, Article=Article, \
                Writer=Writer, Book=Book, Singer=Singer, Song=Song, \
                Citizen=Citizen, City=City, Capital=Capital, \
                Country=Country, Teacher=Teacher, Student=Student, \
                Post=Post, Comment=Comment, Draft=Draft)


# routes and view functions
@app.route("/")
def index():
    form = DeleteNoteForm()
    notes = Note.query.all()
    return render_template("index.html", notes=notes, form=form)


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


# Event listening
class Draft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    edit_time = db.Column(db.Integer, default=0)


@db.event.listens_for(Draft.body, "set")
def increment_edit_time(target, value, oldvalue, initiator):
    if target.edit_time is not None:
        target.edit_time += 1

# same with:
# @db.event.listens_for(Draft.body, 'set', named=True)
# def increment_edit_time(**kwargs):
#     if kwargs['target'].edit_time is not None:
#         kwargs['target'].edit_time += 1
