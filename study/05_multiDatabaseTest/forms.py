# _*_ coding: utf-8 _*_

"""
 author: Xiong Min Xuan
 study, study, and study!!!
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


# Forms
class NewNoteForm(FlaskForm):
    body = TextAreaField("Body", validators=[DataRequired()])
    submit = SubmitField("Save")


class EditNoteForm(FlaskForm):
    body = TextAreaField("Body", validators=[DataRequired()])
    submit = SubmitField("Update")


class DeleteNoteForm(FlaskForm):
    submit = SubmitField("Delete")
